import time
import os
import shutil

delfoldercount = 0
delfilecount = 0

path = input("Enter path to automatically delete files: ")
days = int(input("Enter time to automatically delete files at (in days): "))

seconds = time.time() - (days*86400)

if os.path.exists(path):
	for root, subdirs, files in os.walk(path):
		if seconds >= os.stat(root).st_ctime:
			os.rmdir(root)
			delfoldercount += 1
			break
		else:
			for dir in subdirs:
				subdirpath = os.path.join(root, dir)
				if seconds >= os.stat(root).st_ctime:
					shutil.rmtree(root)
					delfoldercount += 1
			for file in files:
				filePath = os.path.join(root, file)
				if seconds >= os.stat(root).st_ctime:
					os.remove(filePath)
					delfilecount += 1
	else:
		if seconds >= os.stat(root).st_ctime:
			os.remove(path)
			delfilecount += 1
else:
	print("Directory given is nowhere to be found")
	delfilecount += 1
