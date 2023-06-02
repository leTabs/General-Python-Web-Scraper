# importing dependecies
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime
import requests, time , sys

# intoduction
print('--------------------Python General Webscraper--------------------')
print('Provide the inforamtion requested to extract data from a website.')
print('-'*65)
# user data
while True:
    url = input('Enter the URL address : ').strip()
    tag = input('Enter the tag         : ').strip()
    class_name = input('Enter the class\'s name: ').strip()
    print('='*65)
    try:
        web_page = requests.get(url).text
    except:
        print('-'* 23 + ' Invalid URL Adress ' + '-'*22)
        print(f'Did you ment "http://{url}"?')
        print('Please, provide a valid URL adress.')
        print('='*65)
        continue
    if len(tag) == 0:
        print('-'* 24 + ' Invalid HTML tag ' + '-'*23)
        print('Please, provide a valid HTML tag.')
        continue
    break
#parsing
bowl = BeautifulSoup(web_page, 'html.parser')
#finding 
x = ''
o = 1
def find_data():
    global c
    global x
    global o
    if len(class_name) == 0:
        for i in bowl.find_all(tag):
            placeholder = i.text.replace('  ', '').replace('\n', '') 
            x +=  f"{o}) {placeholder} " + '\n' +  '-' * 36 +'\n'
            o+=1
        print(f'{x}')
        c = False
    else:
        for i in bowl.find_all(tag, class_ = class_name):
            placeholder = i.text.replace('  ', '').replace('\n', '') 
            x +=  f"{o}) {placeholder} " + '\n' +  '-' * 36 +'\n'
            o+=1
        print(f'{x}')
        c = True

# asking 
def asking():
    if len(x) == 0:
        print('No results where found')
    else:
        choice = input('Would you like to store this data? ("y"/"n"): ').strip()
        if choice == 'y':
            store_data(c)
        else:
            print('Exiting in: 5 seconds')
            time.sleep(5)
            sys.exit()
# def stroring 
def store_data(c):
    file_name = input('Enter a name for the file: ')
    file_path = Path.home()/'desktop'/ file_name
    time_stamp = str(f'{datetime.now()}').split()
    with open(file_path, 'a') as file:
        #file.write(f'-'*36 + '\n')
        file.write(f'\nStored at: {time_stamp[0]} {time_stamp[1][:5]}\n')
        file.write(f'*'*36 + '\n')
        file.write(x)
    print('-'*50)
    print(f'''Data stored succesfully
Location : Desktop
File Name: "{file_name}.txt"''')
    time.sleep(3)
    close = input('Type enter to close:')
    sys.exit()

#indx = 0
# maeke this in to a function

find_data()
asking()
