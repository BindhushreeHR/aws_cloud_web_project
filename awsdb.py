import pymysql

host="database-1.cuugucm90ioh.us-east-2.rds.amazonaws.com"
port=3306
dbname="pranathi"
user="admin"
password="Pheonix2101"

conn = pymysql.connect(host, user, password, dbname)
