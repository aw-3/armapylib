import os, sys
import ctypes

if sys.platform.lower() == "win32":
    os.system('color')

class color_text():
    black = lambda x: '\033[30m' + str(x) + '\033[0m'
    red = lambda x: '\033[31m' + str(x) + '\033[0m'
    green = lambda x: '\033[32m' + str(x) + '\033[0m'
    yellow = lambda x: '\033[33m' + str(x) + '\033[0m'
    blue = lambda x: '\033[34m' + str(x) + '\033[0m'
    magenta = lambda x: '\033[35m' + str(x) + '\033[0m'
    cyan = lambda x: '\033[36m' + str(x) + '\033[0m'
    white = lambda x: '\033[37m' + str(x) + '\033[0m'
    underline = lambda x: '\033[4m' + str(x) + '\033[0m'
    reset = lambda x: '\033[0m' + str(x) + '\033[0m'


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        return false

def elevate():
    if not is_admin():
        print("Not running as admin. Trying to elevate..")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit(0)