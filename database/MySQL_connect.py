import pymysql
from Mysql_config import host,user,password,database
import os
import pandas as pd

connection = pymysql.connect(
    host= host,
    user= user,
    password= password,
    database= database
)
folder_path = 'your_folder_path'  # 替换为包含Excel和CSV文件的文件夹路径
cursor = connection.cursor()
csv_file = r'D:\sth_funny\citi2024\dataset\股东股本\十大股东.csv'
try:
    df = pd.read_csv(csv_file,skiprows=[0,2],low_memory=False)
    table_name = '十大股东'
    columns = ', '.join(df.columns)
    # print(columns)
    placeholders = ', '.join(['%s' for _ in range(len(df.columns))])
    print(len(columns),len(placeholders))
    print(placeholders)
    sql = "INSERT INTO {} ({}) VALUES ({})".format(table_name,columns,placeholders)
    values = [tuple(row) for row in df.values]
    cursor.executemany(sql, values)
    connection.commit()
except Exception as e:
    connection.rollback()
    print(f"Error importing data from {csv_file}: {str(e)}")
# for filename in os.listdir(folder_path):
#     file_path = os.path.join(folder_path, filename)

#     if filename.endswith('.csv') or filename.endswith('.xlsx'):
#         try:
#             if filename.endswith('.csv'):
#                 df = pd.read_csv(file_path)
#             elif filename.endswith('.xlsx'):
#                 df = pd.read_excel(file_path)
#             for index, row in df.iterrows():
#                 sql = "INSERT INTO your_table_name (column1, column2, column3) VALUES (%s, %s, %s)"
#                 values = (row['column1'], row['column2'], row['column3'])
#                 cursor.execute(sql, values)
#             connection.commit()
#             print(f"Data from {filename} imported successfully.")

#         except Exception as e:
#             connection.rollback()
#             print(f"Error importing data from {filename}: {str(e)}")

cursor.close()
connection.close()