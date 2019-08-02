from sqlalchemy import *
metadata = MetaData()

### Connection ###
engine = create_engine('postgres+psycopg2://srhryast:V1WV12LjQESGf1dALTSbyYOOL7Ifgx8E@john.db.elephantsql.com:5432/srhryast')
test = Table('test', metadata, autoload=True, autoload_with=engine)
con = engine.connect()

### List of schema ###
db_list = inspect(engine).get_schema_names()

query = con.execute('SELECT * FROM minh_phuc_ads.ads_insights LIMIT 1')
data = query.fetchall()
con.close()

print (data[0][0])
