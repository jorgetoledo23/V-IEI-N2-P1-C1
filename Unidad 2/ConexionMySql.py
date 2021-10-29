import mysql.connector
from mysql.connector import (connection)
from mysql.connector import errorcode

try:

  cnx = connection.MySQLConnection(user='root', password='',
                                 host='127.0.0.1',
                                 database='v_eie_p1_c1')


except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  print("Conexion establecida con Exito!")