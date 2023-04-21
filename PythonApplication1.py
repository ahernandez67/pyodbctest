import pyodbc 
cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for SQL Server};Server=myserver;Database=mydatabase;Trusted_Connection=yes')
cursor = cnxn.cursor()	
cursor.execute("SELECT * FROM EMP") 
row = cursor.fetchone() 
while row:
    print (row) 
    row = cursor.fetchone()
