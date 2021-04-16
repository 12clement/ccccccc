import pandas as pd
import pyspark
from pyspark.sql import SparkSession
from src.utils.cleaning_utils import flatten_df
from src.utils.definitions import payment_directcredit_created_mandatory_column_value_list



def get_datatype(df, colname):
    return [dtype for name, dtype in df.dtypes if name == colname][0]

def flatten_and_sort_dataframe(df):
    flat_df = flatten_df(df)
    source_columns = flat_df.columns
    source_columns = sorted(source_columns)
    flat_df = flat_df.select(source_columns)
    return flat_df


def validate_not_null_fields(res_flatten_kafka_source_df):
    pass
     # validate nullable false value kafka_source,s3 and rds
    for field in payment_directcredit_created_mandatory_column_value_list:
        df = res_flatten_kafka_source_df.filter(res_flatten_kafka_source_df[field].isNull())
        assert(df.count() == 0), f"Validation of mandatory field {field} failed"
        print(f"{field} passes not null validation checks")


def compare_dataframe_schemas(dfs):
    """
    Method for comparing datatypes of three different dataframes
    :param dfs:
    :return:
    """
    #  get datatype for the 2 dataframes
    kafka_source_df_type = dfs[0].dtypes
    rds_df_type = dfs[1].dtypes
    assert (kafka_source_df_type == rds_df_type), f"Schema comparison between kafka and rds failed"
    print(f"Kafka schema successfully matches rds schema")


def assert_dataframe_equal_small_payload(res_flatten_kafka_source_df,  res_flatten_rds_df):

    '''
    Due to the volume of data returned by each dataframe we need to split the dataframe
    so that my machine will be able to process each sets of data.
    :param res_flatten_kafka_source_df:
    :param res_flatten_s3_df:
    :param res_flatten_rds_df:
    :return:
    '''

    kafka_pd_df = res_flatten_kafka_source_df.toPandas()
    rds_pd_df = res_flatten_rds_df.toPandas()
    pd.testing.assert_frame_equal(kafka_pd_df, rds_pd_df)
    print(f"Kafka data successfully matches rds data ")

def load_data(spark):
    dataframes = []
    df = spark.read.option("multiline", "true") \
        .json("C:\\Users\\ctagb\\workspace_python\\pythonProject\\pythonProject\\data\\payment_directcredit_created_kafka.json")
    res_flatten_kafka_source_df = flatten_and_sort_dataframe(df)
    for field in res_flatten_kafka_source_df.columns:
        res_flatten_kafka_source_df = res_flatten_kafka_source_df.withColumnRenamed(field, (field.lower()))
    res_flatten_kafka_source_df.printSchema()
    dataframes.append(res_flatten_kafka_source_df)

    df_rds = spark.read.option("multiline", "true") \
        .json("C:\\Users\\ctagb\\workspace_python\\pythonProject\\pythonProject\\data\\payment_directcredit_created_rds.txt")
    res_flatten_rds_df = flatten_and_sort_dataframe(df_rds)
    for field in res_flatten_rds_df.columns:
        res_flatten_rds_df = res_flatten_rds_df.withColumnRenamed(field, (field.lower()))
    res_flatten_rds_df.printSchema()
    dataframes.append(res_flatten_rds_df)
    return dataframes


if __name__ == "__main__":
    spark = SparkSession.builder \
        .master("local[*]") \
        .appName("Feed Demo") \
        .config('spark.sql.execution.arrow.pyspark.enabled', False) \
        .config('spark.sql.session.timeZone', 'UTC') \
        .config('spark.driver.memory', '32G') \
        .config('spark.ui.showConsoleProgress', True) \
        .config('spark.sql.repl.eagerEval.enabled', True) \
        .getOrCreate()

    # Load data from the different sources.
    dfList = load_data(spark)

    # Call method to validate schema
    compare_dataframe_schemas(dfList)

    # Call method to check for nullability of mandatory fields.
    validate_not_null_fields(dfList[0])

    # Call method to compare dataframes values
    assert_dataframe_equal_small_payload(dfList[0], dfList[1])

