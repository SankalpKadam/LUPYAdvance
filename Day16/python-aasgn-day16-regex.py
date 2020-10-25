import requests,re
url="https://study-ccna.com/classes-of-ip-addresses/"
r=requests.get(url)
data=r.text
ip_addresses=r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]"
list_ip=list(set(re.findall(ip_addresses,data)))
for each in list_ip:
	print(each)
#print(data)
