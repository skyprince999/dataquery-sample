import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

def get_mysql_connection():
    # global connection
    # if connection is None or not connection.is_connected():
    connection = mysql.connector.connect(
            host="10.10.23.4",
            user="root",
            password="r00tp@ssw0rd",
            database="bdp"
        )
    return connection



def main():
  conn = get_mysql_connection()
  
  return 

# Run Server
if __name__ == '__main__':
    main()
