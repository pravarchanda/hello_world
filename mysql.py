import sqlalchemy
engine = sqlalchemy.create_engine('mysql://root:123@localhost/mysql') # connect to server
engine.execute("CREATE DATABASE pravar") #create db
engine.execute("show databases") # select new db