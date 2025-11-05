'''
script: cis131_lab_shodan.py
action: A script that takes a quiry and searches shodan, and prints the results from the returned json file 
Date: 11/4/2025
'''

import shodan
import re

# Shodan api key
SHODAN_API_KEY = 'xZLY8glHPMuooSxWZvR2D8tbWPUeZINV'

# Initialize the API
api = shodan.Shodan(SHODAN_API_KEY)

# Initialize the writer
writer = open("shodan_output.txt",'w')

# Search query
query = '"in-tank inventory" state:"AZ"'

try:
	# Perform the search
	results = api.search(query)

	# Iterate through the results for each result in the json file
	for result in results['matches']:
		# Get the values assosiated with the dict key data, use '' if no key is found
		data = result.get('data', '')
		print(data)  # print data
		
		# Write the data to a file, and remove all new line characters, 
		# Removing the \n causes all entries by AVIA to be written correctly, but screws everything else up and vice versa.
		writer.writelines(re.sub(r'[\n]+','',data)+ '\n')
		writer.writelines('\n') # Add new line between results

# If error with the api than print it
except shodan.APIError as e:
	print(f"Shodan API error: {e}")
# Close the writer
writer.close()