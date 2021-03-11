import requests
dictToSend = "Hello" # String to send
res = requests.post("http://localhost:5000/python", json=dictToSend)
dictFromServer = res.json() 
print(f"Response from server: {dictFromServer}") # dictToReturn sends us the server string
