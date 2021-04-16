import pyspark
from pyspark.sql import SparkSession
import pandas as pd

from src.utils.cleaning_utils import flatten_df
from src.utils.definitions import mandatory_column_value_list


def get_datatype(df, colname):
    return [dtype for name, dtype in df.dtypes if name == colname][0]


def flatten_and_sort_dataframe(df):
    flat_df = flatten_df(df)
    source_columns = flat_df.columns
    source_columns = sorted(source_columns)
    flat_df = flat_df.select(source_columns)
    return flat_df


def validate_not_null_fields(res_flatten_kafka_source_df):
    # validate nullable false value kafka_source,s3 and rds
    for field in mandatory_column_value_list:
        df = res_flatten_kafka_source_df.filter(res_flatten_kafka_source_df[field].isNull())
        assert(df.count() == 0), f"Validation of mandatory field {field} failed"
        print(f"{field} passes not null validation checks")


def compare_dataframe_schemas(dfs):
    """
    Method for comparing datatypes of three different dataframes
    :param dfs:
    :return:
    """
    #  get datatype for the 3 dataframes
    kafka_source_df_type = dfs[0].dtypes
    s3_df_type = dfs[1].dtypes
    rds_df_type = dfs[2].dtypes
    assert (kafka_source_df_type == s3_df_type), f"Schema comparison between kafka and s3 failed"
    print(f"Kafka schema successfully matches s3 schema")
    assert (kafka_source_df_type == rds_df_type), f"Schema comparison between kafka and rds failed"
    print(f"Kafka schema successfully matches rds schema")



def assert_dataframe_equal(res_flatten_kafka_source_df, res_flatten_s3_df, res_flatten_rds_df):

    '''
    Due to the volume of data returned by each dataframe we need to split the dataframe
    so that my machine will be able to process each sets of data.
    :param res_flatten_kafka_source_df:
    :param res_flatten_s3_df:
    :param res_flatten_rds_df:
    :return:
    '''

    print('No of all records {}'.format(res_flatten_kafka_source_df.count()))
    out_flatten_kafka_source_df = res_flatten_kafka_source_df.groupBy(
        'payload_policyDetails_features_description').count()
    outList = out_flatten_kafka_source_df.collect()
    feat_desc_lst = []
    for i in outList:
        feat_desc_lst.append(i['payload_policyDetails_features_description'])

    for feat_desc in feat_desc_lst:

        mini_flatten_kafka_source_df = res_flatten_kafka_source_df.filter(res_flatten_kafka_source_df \
                                        ['payload_policyDetails_features_description'] == feat_desc)

        mini_flatten_s3_df = res_flatten_s3_df.filter(
        res_flatten_s3_df['payload_policyDetails_features_description'] == feat_desc)

        kafka_pd_df = mini_flatten_kafka_source_df.toPandas()
        s3_pd_df = mini_flatten_s3_df.toPandas()
        pd.testing.assert_frame_equal(kafka_pd_df, s3_pd_df)
        print(f"Kafka data successfully matches s3 data for fields based on '{feat_desc}'")

        '''
        Only run once kafka dataframe comparison with s3 above is completed and
        commented out
        '''
        # mini_flatten_rds_df = res_flatten_rds_df.filter(
        # res_flatten_rds_df['payload_policyDetails_features_description'] == feat_desc)
        # kafka_pd_df = mini_flatten_kafka_source_df.toPandas()
        # rds_pd_df = mini_flatten_rds_df.toPandas()
        # pd.testing.assert_frame_equal(kafka_pd_df, rds_pd_df)
        # print(f"Kafka data successfully matches rds data for fields based on '{feat_desc}'")

def load_data(spark):
    dataframes = []

    df = spark.read.option("multiline", "true") \
        .json("C:\\Users\\ctagb\\workspace_python\\pythonProject\\pythonProject\\data\\policy_newbusiness_kafka.json")
    res_flatten_kafka_source_df = flatten_and_sort_dataframe(df)
    dataframes.append(res_flatten_kafka_source_df)

    df_s3 = spark.read.option("multiline", "true") \
        .json("C:\\Users\\ctagb\\workspace_python\\pythonProject\\pythonProject\\data\\policy_newbusiness_s3.txt")
    res_flatten_s3_df = flatten_and_sort_dataframe(df_s3)
    dataframes.append(res_flatten_s3_df)

    df_rds = spark.read.option("multiline", "true") \
        .json("C:\\Users\\ctagb\\workspace_python\\pythonProject\\pythonProject\\data\\policy_newbusiness_rds.txt")
    res_flatten_rds_df = flatten_and_sort_dataframe(df_rds)
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
    assert_dataframe_equal(dfList[0], dfList[1], dfList[2])




