import os

dbusr = "postgres"
dbpwd = "YOUR DB PASSWORD HERE"
dbhost = "localhost"
dbengine = "postgresql"
db = "postgres"
cxnstring = (os.environ["DATABASE_URL"] if os.getenv("DATABASE_URL")
    else f"{dbengine}://{dbusr}:{dbpwd}@{dbhost}/{db}")
# cxnstring = "sqlite:///my_db.sqlite"