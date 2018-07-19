import json
import requests
url = 'https://www.metaweather.com/api/location/2306179/2018/7/18/'
r = requests.get(url)
rmesg= json.loads(r.text)
#print(rmesg)
for i in range(len(rmesg)):
	print(rmesg[i]['created'],'',rmesg[i]['applicable_date'],'',rmesg[i]['weather_state_name'])
