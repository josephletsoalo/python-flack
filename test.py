import pyodbc 
import json
import collections

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-4PQLFLU\STOCKFINDERDB;'
                      'Database=tempdb;'
                      'Trusted_Connection=yes;')


#conn = pyodbc.connect('Driver={SQL Server};'
 #                     'Server=DESKTOP-4PQLFLU\STOCKFINDERDB;'
  #                    'Trusted_Connection=yes;')
cursor = conn.cursor()
#creating database
#if cursor.execute("CREATE DATABASE mydatabase")
try:
   cursor.execute("CREATE DATABASE tempdb")
   print("Database created successfully")
except Exception  as e:
   print (str(e))

#creating table
try:
   cursor.execute("CREATE TABLE whatnow (make VARCHAR(255),model VARCHAR(255),year VARCHAR(255),color VARCHAR(255))")
   print("Table created successfully")
except:
   print("Table already exist")

#adding data into the table
try:
    sql = "INSERT INTO whatnow (make, model,year,color) VALUES (?, ?, ?, ?)"
    val = [
      ('BMW', '118i','2012','Red'),
      ('Audi', 'RS3','2020','Blue'),
      ('Mecerdes Benz', 'A45','2019','Gray'),
      ('VW', 'Golf 7 GTi','2019','White'),
      ('Ford', 'Focus ST','2012','Red'),
    ]
    cursor.executemany(sql, val)

    conn.commit()
    print("Data was succesfully inserted")
except:
   print("Table already existError while inserting data")

try:
    sql="SELECT * FROM whatnow"
    rows = cursor.execute(sql)
    
    #array of objects to cenvert the data into json object
    objects_list = []
    for row in rows:
        d = collections.OrderedDict()
        d["make"] = row[0]
        d["model"] = row[1]
        d["year"] = row[2]
        d["color"] = row[3]
        objects_list.append(d)
    j = json.dumps(objects_list)
    print(j)
    
except Exception  as e: 
    ret=""
    print("Error: ",e)
