import colorama
from colorama import Fore, Back, Style
from post import create_app
app = create_app()
def wordpac():
    print(Fore.GREEN + """
                     ▄▄▌ ▐ ▄▌      ▄▄▄  ·▄▄▄▄   ▄▄▄· ▄▄▄·  ▄▄· 
                     ██· █▌▐█▪     ▀▄ █·██▪ ██ ▐█ ▄█▐█ ▀█ ▐█ ▌▪
                     ██▪▐█▐▐▌ ▄█▀▄ ▐▀▀▄ ▐█· ▐█▌ ██▀·▄█▀▀█ ██ ▄▄
                     ▐█▌██▐█▌▐█▌.▐▌▐█•█▌██. ██ ▐█▪·•▐█ ▪▐▌▐███▌
                     ▀▀▀▀ ▀▪ ▀█▄▀▪.▀  ▀▀▀▀▀▀• .▀    ▀  ▀ ·▀▀▀

                    Created by https://github.com/Splintaz
    """)
    print(Style.RESET_ALL)
if __name__ == "__main__":
    wordpac()
    app.run(debug=True)
