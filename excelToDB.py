import pandas as pd
import psycopg2

data = pd.read_excel (r'FILE_PATH')   
df = pd.DataFrame(data)
 
connection = psycopg2.connect(host='localhost',
                        port='5432',
                        user='postgres',
                        password='password',
                        dbname='postgres'
                        )

query=""" INSERT INTO test1 ("First_Name", "Last_Name", "Gender", "Country", "Age", "datee", "Id")
                      VALUES (%s, %s, %s, %s, %s, %s, %s) """

cursor = connection.cursor()

for i in data.itertuples():
    age=str(i.Age)
    date=i.Datee
    date =date.replace("/","-")
    id=str(i.Id)
    toInsert=(i.First_Name,i.Last_Name,i.Gender,i.Country,age,date,id)
    cursor.execute(query,toInsert)
    connection.commit()


