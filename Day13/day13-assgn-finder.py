import os
resp =os.walk("D:\\DATA\\LUPY Advance")
count=0
def findFile(file,count):
	for r,d,f in resp:
		for each in f:
			if file.lower() in each.lower():
				count+=1
				print("\n",each,":",r)
				print("******************************************************")
	return count
file_name = input("Enter the file name ")
count=findFile(file_name,count)
if(count==0):
	print("No file found")