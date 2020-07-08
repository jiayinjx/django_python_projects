import cx_Oracle
con = cx_Oracle.connect('bride2/CS_OraBr1de2_2018@(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=172.24.241.5)(PORT=1521)))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=bridesb1.world)))')

cur = con.cursor()
# cur.execute('select * from TAG order by TYPE')
cur.execute('select * from CARRIER order by ACCRONYM')
res = cur.fetchall()
for r in res:
    print(r)
cur.close()
con.close()