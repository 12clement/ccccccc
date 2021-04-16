from pyspark.sql import functions as f



# api online data
#url = "https://freegeoip.app/json/"

# Making api get call to url
# def httpApiGetMethod():
#     httpdata = urlopen(url).read().decode('utf-8')
#     # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#     # print(httpdata)
#     # print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
#     return httpdata
#
#
# def test_data_value(self):
#     rows = to_date_df(self.df, "M/d/y", "eventdate").collect()
#     for row in rows:
#         self.assertEqual(row["eventdate"], date(2020, 4, 5))
#
#
# def writeDFToDB(df):
#     database = "Sample"
#     table = "dbo.freegeoip"
#     user = "clem"
#     password = "oracle12"
#     #
#     df.write.format("jdbc") \
#         .option("url", f"jdbc:sqlserver://localhost:1433;databaseName={database}") \
#         .option("dbtable", table) \
#         .option("user", user) \
#         .option("password", password) \
#         .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
#         .save()

def flatten_df(nested_df):
    for col in nested_df.columns:
        array_cols = [ c[0]  for c in nested_df.dtypes if c[1][:5] == 'array']
    for col in array_cols:
        nested_df =nested_df.withColumn(col, f.explode_outer(nested_df[col]))

    nested_cols = [c[0] for c in nested_df.dtypes if c[1][:6] == 'struct']

    if len(nested_cols) == 0:
        return nested_df

    flat_cols = [c[0] for c in nested_df.dtypes if c[1][:6] != 'struct']

    flat_df = nested_df.select(flat_cols +
                        [f.col(nc+'.'+c).alias(nc+'_'+c)
                            for nc in nested_cols
                            for c in nested_df.select(nc+'.*').columns])

    return flatten_df(flat_df)
