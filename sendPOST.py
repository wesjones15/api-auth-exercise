# curl -i -X POST -H "ContentType: application/json" -d 
# '{"username":"Wes","password":"starbucks"}' http://0.0.0.0:5000/api/users
import httplib2
import json


def sendPostRequest():
    url = "http://0.0.0.0:5000/api/users"
    
    headers = {"content-type": "application/json"}
    
    data = {
        "username": "Wesley",
        "password": "passcode1"
        }
    # print('\ndata', data)

    body = json.dumps(data).encode('utf8')
    
    # print('\nbody', body)
    
    h = httplib2.Http()
    
    response, content = h.request(uri=url, method="POST", headers=headers, body=body)
    # print("\nresponse",response)
    # print("\ncontent",content)
    
def sendGetRequestWithAuth():
    url = "http://0.0.0.0:5000/api/resource"

if __name__ == '__main__':
    sendPostRequest()