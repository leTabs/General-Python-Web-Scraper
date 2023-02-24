from bs4 import BeautifulSoup
from pathlib import Path
import requests, time, sys # importing the required modules

print('''This is a multi-website web scraper.
In other words, in order to search for the data you want,
all you need to know is the url, the tags and the name of the class in the tag.
Those can be fount be i simple research in the "Elements" of the page while pressing:
Control-Shift-I simultaneously.
''')
# intorduction

def store_in_file(): # this is the function that stores the scraped data
    print('-'*50)
    file_name = input('Enter a name for the file: ')
    file_path = Path.home()/'desktop'/ file_name
    with open(file_path, 'a') as file:
        for i in bowl.find_all(tag, class_= class_name):
            file.write(f'{i.text.replace(" ","")} \n')
    print('-'*50)
    print(f'The data are stored in a txt file, named "{file_name}". On your Desktop!')
    time.sleep(10)

# the user inputs the requirements for the data they what...
url = input('Enter the specific url: ').strip()
tag = input('Enter a tag           : ').strip()
class_name = input('Enter the class name  : ').strip()

# the requests and bs4 modules take place
web_page = requests.get(url).text
bowl = BeautifulSoup(web_page, 'html.parser')
print('-'*50)
x=''
indx = 0
for i in bowl.find_all(tag, class_= class_name):
    indx += 1
    x = i.text
    print(f"{indx}) {x.replace(' ', '')}")
if len(x) == 0:
    print('Sorry, no results where found.') #safety conditions
    print('*'*50)
    close = input('Typer enter to close: ')
    sys.exit()
if len(x) != 0: # if there is a result, the user gets asked if they what to store the data
    print('='*50)
    choice = input('Would you like to store this data? ("y"/"n"): ').strip()
    if choice == 'y':
        store_in_file() # if yes the call the respective function
    if choice != 'y':
        time.sleep(1)
        print('-'*50)
        print('Have a beautiful day.')
        time.sleep(3)
        sys.exit()



