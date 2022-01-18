#Main
from xss import XssScanner
from time import sleep 
import argparse

def _run(url,data):
    #print('-u '+args.domaine+"\nWordlist : "+args.wordlist)
    #url = 'http://challenge01.root-me.org/web-client/ch24/?nickname=' 
    wordlist = "files/wordlist/low.txt"
    if data != False:
        print('Set send POST')
        methode = 'post'
        print(data)
    else:
        methode = 'get'

    try:

        print('URL SET : ' + url)
    except:
        pass
    
    thread = 2
    proxy = False
    lunch = XssScanner(url, wordlist, methode, proxy)
    lunch.run()

def __main():
    data = False
    parser = argparse.ArgumentParser(prefix_chars='-')
    parser.add_argument('-l', type=str, help='URL type is https://link.com/?data1={{inject}}&?data2={{inject}}\nPayload injected in "inject"')
    #parser.add_argument('-b64', type=bool,help='Encode base64 payload')

    try:
        parser.add_argument("-d", required=False, help='Use data POST send data1={{inject}}#data2={{inject}}\nPayload injected in "inject"')

    except:
        pass
    #parser.add_argument("-w", "--wordlist", help='Payload list to look for XSS vulnerabilities')
    args = parser.parse_args()
    if not args.d:
        sleep(0.5)
        args.d = False
        print('Send GET data : http://localhost/xsstest.php?q={{inject}}')
    if not args.l:
        sleep(0.5)
        args.l = 'http://localhost/xsstest.php?q={{inject}}'
        if args.d != False:
            args.l = 'http://localhost/xsstest.php'
        print('default url :'+args.l)
    return args


print(" _   _     _       _       _   _                  _ _       _     \n| |_| |__ (_)___  (_)___  | |_| |__   ___    __ _(_| |_ ___| |__  \n| __| '_ \| / __| | / __| | __| '_ \ / _ \  / _` | | __/ __| '_ \ \n| |_| | | | \__ \ | \__ \ | |_| | | |  __/ | (_| | | || (__| | | |\n \__|_| |_|_|___/ |_|___/  \__|_| |_|\___|  \__, |_|\__\___|_| |_|\n                                            |___/                 \n")
if __name__ == '__main__':
    print('With run use\npython3 ./main.py -l https://link.com/?data1={{inject}}&?data2={{inject}}\n\nIf you use post data\npython3 ./main.py -d data1={{inject}}#data2={{inject}}&data3=text -l https://link.com/\n\n')

    parse = __main()
    _run(parse.l, parse.d)
    