### Improve query performance by increasing the number of rows returned in each batch from Oracle to the Python program
import time
import cx_Oracle

con = cx_Oracle.connect('bride2/CS_OraBr1de2_2018@(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=172.24.241.5)(PORT=1521)))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=bridesb1.world)))')

start = time.time()

cur = con.cursor()
cur.arraysize = 2000
cur.execute('select * from RULE')
res = cur.fetchall()
# print(res)  # uncomment to display the query results

elapsed = (time.time() - start)
print(elapsed, "seconds")

cur.close()
con.close() 