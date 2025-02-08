import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import urllib.parse

password = "r00tp@ssw0rd" 


def get_mysql_connection():
    # global connection
    # if connection is None or not connection.is_connected():
    enc_pwd = urllib.parse.quote(password)
  
    connection = mysql.connector.connect(
            host="10.10.23.4",
            user="root",
            password="r00tp@ssw0rd",
            database="bpd"
        )
    
    engine = create_engine(f"mysql+pymysql://root:{enc_pwd}@10.10.23.4:3306/bpd")
    
    return connection, engine


#Need to add some code for populating the tables
def main():
    
  conn, engine = get_mysql_connection()
    
  cursor = conn.cursor()
  
  #Show existing databases
  databases = ("show databases")
  cursor.execute(databases)
  for (databases) in cursor:
      print(databases)

  #Show existing tables
  query = "SELECT * FROM information_schema.tables WHERE table_schema = 'bpd';"
  cursor.execute(query)
  record = cursor.fetchall()
  print("You're connected to database: ")
  for table in record:
      print(table)

  engine.dispose()
  conn.close()
  return 

# Run Server
if __name__ == '__main__':
    main()
