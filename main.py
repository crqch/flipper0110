import os
import subprocess
import time

from colorama import Fore, Style

from functions import manager
from menu_handler import get_menu

VERSION = "0.0.1"
AUTHORS = "crqch"

manager.main()


class Main:
    def __init__(self):
        os.system("title " + "flipper0110 - " + VERSION)
        print(f"""{Fore.LIGHTYELLOW_EX}
__________________________________________________________ ╨╨▓@╓____________________________________________
____________________,╖╖@²²²²²²²²╙W╖╖╖______________________╖╖_ ╙╫W__________________________________________
_______________,,m╝╙╙╙╙╙╙╙╙mm,,,m▒"  ,╫Ñm╖________________  ╙╚▓╖ ╙╫Ç________________________________________
____________ ,@╜ ___________╓▒▒╨`_ ,* _^, ╨╖______________ ╨╬╖ ╟▓_ ▓m_______________________________________
____________╢╜ ____________╓▒╫╜__╓╜ _ *_ ╙_╟@___╖@*****╖╖___ ╜_ ╜`_╙╜_______________________________________
___________╚_______╓m╙▒▒▒▒╙Ñ@C__j▒__ )_ ,m╜ ▒Ñ╜` ____,,╥╥▓__________________________________________________
_________________¿`∩" ,,, "*,*,_ `«,,∩*"_,*"_____,æ╬▓╢╢╢╝ __________________________________________________
________________╢╓╜_╫╣╣╣╢╣▓U ╖░H__   _╓*` ____ ╓@╣╢╢╢▓╜ ____________________________________________________
________________▒╟_╟╢╢w╫╢╢╢╢_╟░C_,≡²╙ _______╓▓╢╢╢╢▓╜_______________________________________________________
_____________,∩¿╣╙,'╫╢╢╢▓╩╩╩H╟ ╙" _________╓▓╢╢╢╢▓"_________________________________________________________
____________▒▒▒▒▒@╙╖╓╜`  ___  ___________g▓╢╢╢╢▓`___________________________________________________________
____________▒▒▒▒▒▒▒▓ _________________,@╣╝     ╜╜▒▒_  _,╓╜╙U________________________________________________
____________ `▒▒╜╜_ ________ )m,,,╥m▓▓╢╢,,,,,,,,nmm╜╙╙_ _,g─________________________________________________
______________________________                  ____ __,@╜__________________________________________________
_________________________________________________╖╓M╜╜   ___________________________________________________
________________________________________,╓╥@▓▓Ñ  ___________________________________________________________
______________________________________ ╣╫▓╣╢╢╢______________________________________________________________
_______________________________________ `╜▒▒▒╫╣_____________________________________________________________
____________________________________________________________________________________________________________
____________________________________________________________________________________________________________
___╟▓╨╨╨╨╨╨╨╜_╓╣________╓╣_,╫Ñ╨╨╨╨╫▓▓`╓╣╨╨╨╨╨▓╣Ñ_╟▓╨╨╨╨╨╨╨`,╫Ñ╨╨╨╨╫▓▓╜_______ dP"Yb    .d   .d  dP"Yb_______
__╫▓@@@@@M___]╣`_______]╣`,▓▓@@@@@▓`_]╣╫@@@@╬╝ _╫▓@@@@@M__,▓▓@@@@@╣`_________dP   Yb .d88 .d88 dP   Yb______
_╬Ñ_________g╢mmmmmmm_g▓ ╓╣┘________g▓ ________╬╣mmmmmmm_╓╣┘____ ╙╫@,________Yb   dP   88   88 Yb   dP______
╩╜__________        __ __  _________ _________         __  _______  ╩`_______ YbodP    88   88  YbodP_______

{Fore.LIGHTGREEN_EX}flipper0110 v.{VERSION}
{Fore.LIGHTGREEN_EX}Authors: {AUTHORS}
{Fore.LIGHTGREEN_EX}Github: https://github.com/crqch/flipper0110
        """)
        input("Press enter to PLAY!")
        self.choice()

    def choice(self):
        os.system('cls')
        print(Fore.LIGHTYELLOW_EX + "-" * 60)
        for key, value in get_menu().items():
            print(f"{Fore.LIGHTYELLOW_EX} [{key}] - {value[0]}")
        print(Fore.LIGHTYELLOW_EX + "-" * 60)
        try:
            choice = int(input(f"{Fore.LIGHTYELLOW_EX} > "))
            if choice in get_menu():
                try:
                    get_menu()[choice][1]()
                finally:
                    self.choice()
            else:
                print(f"{Fore.LIGHTRED_EX} Invalid choice!")
                self.choice()
        except ValueError:
            print(f"{Fore.LIGHTRED_EX} Invalid choice!")
            self.choice()


if __name__ == '__main__':
    try:
        Main()
    except KeyboardInterrupt:
        print(f"{Fore.RED}\n\nExiting...{Style.RESET_ALL}")
        exit(0)
