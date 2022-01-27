import threading
import time

def usless_function(seconds):
	print(f"Waiting for {seconds}",end = "\n")
	time.sleep(seconds);
	print(f"Done Waiting {seconds}")


for x in range(4):
	th = threading.Thread(target=usless_function,args=[x])

	th.start();
