import os
from configparser import ConfigParser
config=ConfigParser()
config.read("config-file.ini")
dir=config.get("EXT","CurrentPath")
from=config.get("EXT","from")
to=config.get("EXT","to")
os.chdir(dir)
for file in os.listdir("."):
	if file.endswith(from):
		first_name=file.rsplit(".",1)[0]
		new_name=first_name+to
		print(file+" changed to -> "+new_name)
		os.rename(file,new_name)
