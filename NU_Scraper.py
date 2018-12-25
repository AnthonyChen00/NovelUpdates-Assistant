import requests, lxml.html
import getpass
import sys
from bs4 import BeautifulSoup
from novel import Novel

def login():
    username = input("Enter your NovelUpdates Username: ")
    password = getpass.getpass("Enter your NovelUpdates Password: ")
    return username, password

def scrapper(username, password):
    # logs onto website and pulls in the data from reading list onto a file
    s = requests.session()
    response = s.get('https://www.novelupdates.com/login/', timeout = 5)
    if response.status_code == 200:
        login_html = lxml.html.fromstring(response.text)
        hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
        form = {x.attrib["name"]:x.attrib["value"] for x in hidden_inputs}
        form['log'] = username
        form['pwd'] = password
        response = s.post('https://www.novelupdates.com/login/',data=form)

        if response.url == 'https://www.novelupdates.com/':
            print("\t  ===Login Sucess===")
            reading_list = s.get('https://www.novelupdates.com/reading-list/')
            return reading_list.text
        else:
            print("Error: Unable to log on, please check credentials")
            sys.exit()
    else:
        print("Failure to access login page")
        sys.exit()

def html_parse(html):
    reading_list = []
    soup = BeautifulSoup(html,'html.parser')
    print("\t Parsing Reading List")
    print(" ====================================")
    title_names = soup.find_all("tr",attrs={"class":"rl_links"})
    chapters = soup.find_all("a",attrs={"class":"chp-release"})
    counter = 0;
    if (len(chapters)%2) != 0:
        print("Error: Incorrect number of chapters")
        sys.exit()
    for i in range(len(title_names)):
        title = title_names[i].attrs["data-title"]
        current_chapter = chapters[i + counter].get_text()
        latest_chapter = chapters[i+ counter + 1].get_text()
        counter += 1
        temp = Novel(title,latest_chapter, current_chapter)
        reading_list.append(temp)
    return(reading_list)

def newChapters(reading_list, userPrint):
    numOfCh = 0
    for novel in reading_list:
        if novel.new_update():
            if userPrint:
                print(" -  " + novel.title)
            else:
                numOfCh += 1
    if userPrint:
        return 0
    return(numOfCh)

def promptTitles(updates):
    userInput = "n"
    if updates > 1:
        print("There are " + str(updates) + " chapters released!")
        userInput = input("Show which novel titles? (y/n)")
    elif updates == 1:
        print("There is a new chapter released!")
        userInput = input("Show the novel title? (y/n)")
    while (userInput != 'n' and userInput != 'y'):
        print("Error: Invalid Input")
        if updates > 1:
            userInput = input("Show which novel titles? (y/n)")
        elif updates == 1:
            userInput = input("Show the novel title? (y/n)")
    if userInput == "y":
        if updates > 1:
            print("The updates are for: ...")
        elif updates == 1:
            print("The update is for: ... ")
        return True
    else:
        return False

if __name__ == '__main__':
    username, password = login()
    html_string = scrapper(username,password)
    readingList = html_parse(html_string)
    updates = newChapters(readingList, userPrint=False)
    userPrint = promptTitles(updates)
    updates = newChapters(readingList, userPrint)
