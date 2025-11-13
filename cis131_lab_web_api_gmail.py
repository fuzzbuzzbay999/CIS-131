'''
script: cis131_lab_web_api_gmail.py
action: A script that takes a search query results from shodan and emails it to someone
Date:   11/12/2025
'''
	

import shodan
import json
import ezgmail


#Initialize the Shodan API key
api = shodan.Shodan('xZLY8glHPMuooSxWZvR2D8tbWPUeZINV')
query = "'in-tank inventory' state:'AZ'"

#Initialize ezgmail and start a blank message
# Note that credientials.json must exist in the same folder as this script
ezgmail.init()
msg = ""

#Execute the Shodan query
result = api.search(query)

# Shodan returs a dictionary of 'matches' and 'total'
matches = result["matches"]

# Matches is a json string so we convert it to json and then into a dictionary  
inputdata = json.dumps(matches)
datadict = json.loads(inputdata)

# datadict is a list of dictionary items, one item for earch result
# append the data from each results and include a carriage return
for i in datadict:
	for key,value in i.items():
		msg += i["data"] + "\r"

# send the email
ezgmail.send('djuliano@mail.pima.edu','Internet Gas Gauges in AZ',msg)
