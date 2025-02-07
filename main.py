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


def get_financial_year(date):
    if date.month >= 4:
        return f"{date.year}-{date.year + 1}"
    else:
        return f"{date.year - 1}-{date.year}"
    

def financial_year(data, date_column):
    """
    Function to add a 'Financial Year' column based on a specific date column.
    """
    # Convert the date column to datetime if not already
    data[date_column] = pd.to_datetime(data[date_column], errors='coerce')

    # Apply the get_financial_year function to the date column
    data["financial_year"] = data[date_column].apply(get_financial_year)

    return data


def map_catalog(data):
    __, engine = get_mysql_connection()

    table_name = "catalog"
    query = f"SELECT * FROM {table_name}"
    catalog = pd.read_sql(query, con=engine)
    print(f"catalogue cols : {catalog.columns}")
    data = data.merge(catalog, how="left", on="material_code")
    
    data.drop(["material_description_y", "count_of_material_code"], inplace=True, axis=1) 
    
    data.rename(columns={"material_description_x": "material_description"}, inplace=True)
    print(data.columns)
    print("Completed mapping catalog IDs")
    engine.dispose()
    return data


#Need to add some code for populating the tables
def main():
    
  conn, engine = get_mysql_connection()
    
  cursor = conn.cursor()
  
  #Show existing databases
  databases = ("show databases")
  cursor.execute(databases)
  for (databases) in cursor:
      print(databases)

  # #Populate Material code
  # df = pd.read_excel("MatCat_Mapping_NOV2024.xlsx")
  # print(f"Catalog : {df.shape}")
  # print(f"Catalog cols: {df.columns}")
  # df.to_sql("catalog", con=engine, if_exists="replace", index=False)

  # #Populate GRN data 
  # df = pd.read_excel("grnreport_nov.XLSX")
  # print(f"GRN : {df.shape}")

  # df.rename(str.lower, axis='columns', inplace=True)
  # for col in df.columns:
  #   new_col = col.replace(" ", "_")
  #   # print(col, new_col)
  #   df.rename(columns={col: new_col}, inplace=True)
  
  # df = financial_year(df, "document_date")
  # df = map_catalog(df)
  # print(f"GRN cols: {df.columns}")
  # df.to_sql("grnreport", con=engine, if_exists="replace", index=False)

  #Populate Purchase data 


  #Populate Stock Statement data 

  
  #Populate Reservation data 



  #Populate TECO data 


  #Populate CLM data


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
