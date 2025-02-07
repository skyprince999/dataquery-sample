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
    
    engine = create_engine(f"mysql+pymysql://root:{enc_pwd}@10.10.23.4:3036/bpd")
    
    return connection, engine


#Need to add some code for populating the tables
def main():
    
  conn, engine = get_mysql_connection()
    
  cursor = conn.cursor()
  databases = ("show databases")
  cursor.execute(databases)
  for (databases) in cursor:
      print(databases)
      
  df = pd.read_excel("MatCat_Mapping_NOV2024.xlsx")
  print(df.shape)
  df.to_sql("catalogue", con=engine, if_exists="replace", index=False)
  engine.dispose()
  conn.close()
  return 

# Run Server
if __name__ == '__main__':
    main()
