import pyodbc 
import json
import collections
               
class DBHelper():

    def __connect__(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-4PQLFLU\STOCKFINDERDB;'
                      'Database=tempdb;'
                      'Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()
        try:
           self.cursor.execute("CREATE TABLE stockTable(make VARCHAR(255),model VARCHAR(255),year VARCHAR(255),color VARCHAR(255))")
           
        except Exception as e:
           print("Table ERROR! ", e)

    #disconnect from database
    def __disconnect__(self):
        self.conn.close()

    def _add(self,form):
        #adding data into the table
        
        try:
            sql = "INSERT INTO stockTable (make, model,year,color) VALUES (?, ?, ?, ?)"
            
            self.__connect__()
            self.cursor.execute(sql, form.make.data,form.model.data,form.year.data,form.color.data)
            self.conn.commit()
            self.__disconnect__()
            
        except Exception as e:
           print("Adding Data ERROR! ",e)
           self.__disconnect__()

    #get data from the table
    def _getData(self):
        
        try:
            sql="SELECT * FROM stockTable"
            self.__connect__()
           
            rows = self.cursor.execute(sql)
            #array of objects to cenvert the data into json object
            
            objects_list = []
            for row in rows:
                d = collections.OrderedDict()
                d["make"] = row[0]
                d["model"] = row[1]
                d["year"] = row[2]
                d["color"] = row[3]
                objects_list.append(d)

            #convet the data into json
            ret = json.dumps(objects_list)
            self.__disconnect__()
           
            return ret
        except Exception as e: 
            print("Geting Data ERROR! ",e)
            ret=[]
            self.__disconnect__()
            return ret

       

