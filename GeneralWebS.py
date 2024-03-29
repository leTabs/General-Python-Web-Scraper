# impoer dependencies 

from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime
import requests, time , sys

# introduction to the users

print('----------------------- General Webscraper ----------------------')
print('Provide the inforamtion requested to extract data from a website.')
print('-'*65)


# the user provides the necessary data 

while True:
    url_address = input('URL Adress           : ').strip()
    html_tag    = input('HTML tag             : ').strip()
    class_name  = input('The tag\'s class name : ').strip()
    print('='*65)
    try: 
        web_page = requests.get(url_address).text
    except:
        print('-'* 23 + ' Invalid URL Adress ' + '-'*22)
        print(f'Did you ment "http://{url_address}"?')
        print('Please, provide a valid URL adress.')
        print('='*65)
        continue
    if len(html_tag) == 0:
        print('-'* 24 + ' Invalid HTML tag ' + '-'*23)
        print('Please, provide a valid HTML tag.')
        continue
    break


# parsing the web page & declaring the necessary variables

bowl = BeautifulSoup(web_page, 'html.parser')
scraped_data = ''
indx = 1
all_tags = ''


# the function that scrapes the page according to the user's data

def scrape_page():
    global scraped_data
    global indx
    global all_tags
    if len(class_name) == 0:
        for item in bowl.find_all(html_tag):
            filtered_item = item.text.replace('  ', '').replace('\n', '') 
            scraped_data += f"{indx}) {filtered_item}" + '\n' + '-'* 65 + '\n'
            indx += 1
        print(found_data() if scraped_data else no_results())
        all_tags = False
    else:
        for item in bowl.find_all(html_tag, class_ = class_name):
            filtered_item = item.text.replace('  ', '').replace('\n', '') 
            scraped_data += f"{indx}) {filtered_item}" + '\n' + '-'* 36 + '\n'
            indx += 1
        print(found_data() if scraped_data else no_results())
        all_tags = True



# the function displays the data for the user and asks if they want to store them

def found_data():
    print('-'*25+' Scraped Data '+ '-'*26)
    print('='*65)
    print(scraped_data)
    choice = input('Would you like to store this data? ("y"/"n"): ').strip().lower()
    if choice == 'y':
        store_data(all_tags)
    else:
        terminate()



# the function notifies the user that no data were discovered

def no_results():
    print('No result found.')
    terminate()



# the function that is responsible of the data storing

def store_data(present_class_name):
    file_name = input("Enter the file's name: ").strip()
    file_path = Path.home() / 'desktop' / file_name
    time_stamp = str(f'{datetime.now()}').split()
    
    with open (file_path, 'a') as file:
        file.write(f'\nStored at: {time_stamp[0]} {time_stamp[1][:5]}\n')
        file.write(f'From     : {url_address}\n')
        file.write(f'*'*130 + '\n')
        file.write(scraped_data)
    print('-'*50)
    print(f'''Data store succesfully
Location : Desktop
File Name: "{file_name}.txt"''')
    terminate()



# the function that is responsible of terminating the aplication

def terminate():
    time.sleep(2)
    print('. . . . . '* 8)
    close = input('Type "ENTER" to terminate:')
    sys.exit()


# calling the root function
scrape_page()
