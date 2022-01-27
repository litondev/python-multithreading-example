import mysql.connector 
import threading
import time

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost", 
  user="root",
  password="root",
  database="crm_mediatama",
  use_pure=True
)

def insert_data(thread):
	for x in range(100000):
		print(f"Insert Data {x} in {thread}");
		time.sleep(1);
	
for x in range(10):
	th = threading.Thread(target=insert_data,args=[x])
	th.start();