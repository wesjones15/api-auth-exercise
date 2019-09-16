from sendPOST import sendGetRequestWithAuth


 #TEST 1 TRY TO MAKE A NEW USER
try:
	url = address + '/users'
	h = Http()
	#h.add_credentials('TinnyTim', 'Udacity')
	data = dict(username = "TinnyTim", password = "Udacity")
	data = json.dumps(data)
	resp, content = h.request(url,'POST', body = data, headers = {"Content-Type": "application/json"})
	if resp['status'] != '201' and resp['status'] != '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])
except Exception as err:
	print("Test 1 FAILED: Could not make a new user")
	print(err.args)
	sys.exit()
else:
	print("Test 1 PASS: Succesfully made a new user")