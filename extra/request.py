# O-Pac (Office Program and Control) allows you to send remote commands and receive encrypted data with a Word/Excel/PowerPoint Macro.
# Created by https://github.com/Splintaz/
import requests
dictToSend = "Hello" # String to send
res = requests.post("http://127.0.0.1:5000/python", json=dictToSend)
dictFromServer = res.json() 
print(f"Response from server: {dictFromServer}") # dictToReturn sends us the server string
