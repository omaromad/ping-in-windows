import subprocess
import pyfiglet
import time
from colorama import Fore
import sys
sex = (Fore.WHITE)
text = pyfiglet.figlet_format("WEB HACK")
print( sex ,text)
while True:
    try:
        command = input ("scango.com>")
        if command.lower() ==  "stop":
            break

        output = subprocess.run(["ping", command],shell=True,capture_output=True)
        print(output)


    except Exception:
       continue

time.sleep(8)
print("____________________________________________________________________________________________________________________")
sys.exit()
