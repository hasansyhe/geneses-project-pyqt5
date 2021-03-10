import os
import guilib
key = open("key.key", "r")
key_new = key.read()
if(key_new == "sflma"):
	os.system("python3 splash.py")
	guilib.run()
else:
	print("Error Your Key is not true")
