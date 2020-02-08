#! python3      #For linux write src/bin/python3 instead of python3
#passwordManage.py - An insecure password locker program

import sys, pyperclip # problem importing pyperclip

passwords = {'outlook': '123454321',
             'gmail': 'abrakatabra',
             'yahoo': '666'}

if sys.argv<2 :
    print("Don't forget to give account as parameter")
    sys.exit()
account = sys.atgv[1]
if account in passwords.keys():
    password = passwords[account]
    pyperclip.copy(password)
    print('Password for account ' + account + 'copied to clipboard')
else:
    print('There is no account named ' + account + ' in the database.')
