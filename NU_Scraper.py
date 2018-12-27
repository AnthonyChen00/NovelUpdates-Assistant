import requests, lxml.html
import getpass
import sys
from bs4 import BeautifulSoup
from novel import Novel
from settings import Settings
import os
import time
def login():
    username = input("Enter your NovelUpdates Username: ")
    password = getpass.getpass("Enter your NovelUpdates Password: ")
    return username, password

def scrapper(username, password):
    # logs onto website and pulls in the data from reading list onto a file
    print("\tLogging in to NovelUpdates")
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

def html_parse(html, fileHandle):
    """fileHandle is a work in progress feature of creating a reading list offline"""
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
    if fileHandle:
        for i in range(len(title_names)):
            title = title_names[i].attrs["data-title"]
            current_chapter = chapters[i + counter].get_text()
            latest_chapter = chapters[i+ counter + 1].get_text()
            counter += 1
            temp = Novel(title,latest_chapter, current_chapter)
            reading_list.append(temp)
        return(reading_list)
    else:
        saveFile = open("readingList.txt","w")
        counter = 0
        for i in range(len(title_names)):
            saveFile.write(title_names[i].attrs["data-title"] + ",")
            saveFile.write(chapters[i + counter].get_text() + ",")
            saveFile.write(chapters[i+ counter + 1].get_text() + "\n")
            counter += 1
        print("The save file,'readingList.txt' has been created...")
            # temp[2][0:len(temp[2])-1]


def fileReader():
    if os.path.isfile("readingList.txt") == False:
        print("Error: Save file, 'readingList.txt' is missing")
        sys.exit()
    readingList = []
    saveFile = open("readingList.txt","r")
    line = saveFile.readline()
    while(len(line) != 0):
        data = line.split(",")
        newNovel = Novel(data[0], data[1], data[2][0:len(data[2])-1])
        readingList.append(newNovel)
        line = saveFile.readline()
    return readingList

def newChapters(reading_list):
    updates = []
    for novel in reading_list:
        if novel.new_update():
            updates.append(novel.title)
    print("There are " + str(len(updates)) + " new updates...")
    for i in range (len(updates)):
        print(" " + str(i) + " - " + updates[i])
    return 0

def printAll(reading_list):
    print("\n\tCurrent Reading List:")
    for novel in reading_list:
        novel.printNovel()

if __name__ == '__main__':
    while(1):
        config = Settings()
        if config.prompt:
            if config.offload:
                username = config.username
                password = config.password
                if config.scheduled:
                    while(1):
                        try:
                            print("Begining to Scheduled Action")
                            time.sleep(config.pause) #pauses for an hour
                            currentHour = time.localtime(time.time()).tm_hour
                            if str(currentHour) in config.times:
                                html_string = scrapper(username,password)
                                readingList = html_parse(html_string, fileHandle=True)
                                updates = newChapters(readingList)
                                print('\n')
                        except KeyboardInterrupt:
                            print("\nEnding program")
                            sys.exit()
                else:
                    html_string = scrapper(username,password)
                    readingList = html_parse(html_string, fileHandle=True)
                    updates = newChapters(readingList)
                    sys.exit()
            else:
                username, password = login()
                html_string = scrapper(username,password)
                readingList = html_parse(html_string, fileHandle=True)
                updates = newChapters(readingList)
                sys.exit()
        else:
            username, password = config.initialization()
            html_string = scrapper(username,password)
            readingList = html_parse(html_string, fileHandle=True)
            # readingList = fileReader()
            updates = newChapters(readingList)
            if config.scheduled:
                print("Begining to Scheduled Action")
                while(1):
                    try:
                        time.sleep(3600) #pauses for an hour
                        currentTime = time.localtime(time.time())
                        currentHour = currentTime.tm_hour
                        if str(currentHour) in config.times: #will change to add options of changing the settings
                            html_string = scrapper(username,password)
                            readingList = html_parse(html_string, fileHandle=True)
                            updates = newChapters(readingList)
                    except KeyboardInterrupt:
                        print("\nEnding program")
                        sys.exit()
            else:
                sys.exit()
