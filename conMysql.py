import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='mysql')
cur = conn.cursor()
cur.execute("SELECT Host,User FROM user")
print(cur.fetchall())
cur.close()
conn.close()
