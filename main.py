# OC2 (Office Command and Control) allows you to send remote commands and receive encrypted data with a Word/Excel/PowerPoint Macro.
# Created by https://github.com/Splintaz/
import colorama
from colorama import Fore, Back, Style
from post import create_app
app = create_app()
def opac():
    print(Fore.GREEN + """
    Office Command and Control
Created by https://github.com/Splintaz
""")
    print(Style.RESET_ALL)
if __name__ == "__main__":
    opac()
    app.run(host="0.0.0.0", port="4444")
