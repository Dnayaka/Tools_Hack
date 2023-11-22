import os
import subprocess
os.system("clear")
print("""\033[96m \033[1m

          ██╗░░██╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗░██████╗░
          ██║░░██║██╔══██╗██╔══██╗██║░██╔╝██║████╗░██║██╔════╝░
          ███████║███████║██║░░╚═╝█████═╝░██║██╔██╗██║██║░░██╗░
          ██╔══██║██╔══██║██║░░██╗██╔═██╗░██║██║╚████║██║░░╚██╗
          ██║░░██║██║░░██║╚█████╔╝██║░╚██╗██║██║░╚███║╚██████╔╝
          ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░
                ████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
                ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
                ░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
                ░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
                ░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
                ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░
                                 V 0.0.2
                      Type menu for see the tools
""")
def menu():
    p = input("╚════> ")
    if p == "menu" or p == "Menu":
        print("""
         ╔═════════════════════════════════════════════════════╗
        ╔╩════════╦════════════════════════════════════╦═══════╩═╗
        ║ ╔═══════╩════════════════════════════════════╩═══════╗ ║
        ║ ║  1. DDOS                            2. PHISING     ║ ║
        ║ ║  3. CRACKER FB                      4. IP TRACKER  ║ ║
        ╚═╣  5. SPAM                            0. SETUP TOOLS ╠═╝
          ╚════════════════════════════════════════════════════╝
        """)
        menu()
    elif p == "0":
        os.system("python setup.py")
        os.system("clear")
        os.system("python main.py")

    elif p == "1":
        q = input("[?]Do you complete install the setup?(Y/N): ")
        if q == "Y" or q == "y":
            os.system("python HASOKI/main.py")
        elif q == "N" or q == "n":
            os.system("python setup.py")
            menu()
        else:
            input("[>]Option not available")
            menu()

    elif p == "2":
        q = input("[?]Do you complete install the setup?(Y/N): ")
        if q == "Y" or q == "y": 
            os.system("python MaxPhisher/maxphisher.py")
        elif q == "N" or q == "n":
            os.system("python setup.py")
            menu()
        else:
            input("[>]Option not available")
            menu()
    elif p == "3":
        q = input("[?]Do you complete install the setup?(Y/N): ")
        if q == "Y" or q == "y":
            os.system("python CRACK_FB/SMBF.py")
        elif q == "N" or q == "n":
            os.system("python setup.py")
            menu()
        else:
            input("[>]Option not available")
            menu()
    elif p == "4":
        q = input("[?]Do you complete install the setup?(Y/N): ")
        if q == "Y" or q == "y":
            os.system("python GhostTrack/GhostTR.py")
        elif q == "N" or q == "n":
            os.system("python setup.py")
            menu()
        else:
            input("[>]Option not available")
            menu()
    elif p == "5":
        q = input("[?]Do you complete install the setup?(Y/N): ")
        if q == "Y" or q == "y":
            os.system("python TBomb/bomber.py")
        elif q == "N" or q == "n":
            os.system("python setup.py")
            menu()
        else:
            input("[>]Option not available")
            menu()

    else:
        input("[>]Option not available")
        menu()

menu()
