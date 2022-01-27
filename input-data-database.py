import mysql.connector 
import threading
import time

import mysql.connector

def insert_data(thread):
	mydb = mysql.connector.connect(
  		host="localhost", 
  		user="root",
  		password="root",
  		database="crm_mediatama",
  		use_pure=True
	)

	mycursor = mydb.cursor()

	datas = [];

	for x in range(10000):	
		datas.append(("2020-01-01",1,1,f"Des-{x}","defualt.png","image","2020-02-02","TKJ"))	
		print(f"Insert Data {x} in {thread}");
		# time.sleep(1);		

	sql = "INSERT INTO visits (date, user_id, school_id, discription, attachment, attachment_type, next_date, major) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
	mycursor.executemany(sql, datas)
	mydb.commit()
	print(mycursor.rowcount, "was inserted.") 
	# print(datas);

for p in range(10):	
	for x in range(10):
		th = threading.Thread(target=insert_data,args=[x])
		th.start();
