import requests, lxml.html
import getpass
import sys
from bs4 import BeautifulSoup

def login():
    username = input("Enter your NovelUpdates Username: ")
    password = getpass.getpass("Enter your NovelUpdates Password: ")
    return username, password

def scrapper():
    # logs onto website and pulls in the data from reading list onto a file
    s = requests.session()
    response = s.get('https://www.novelupdates.com/login/', timeout = 5)
    if response.status_code == 200:
        login_html = lxml.html.fromstring(response.text)
        hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
        form = {x.attrib["name"]:x.attrib["value"] for x in hidden_inputs}
        username, password = login();
        form['log'] = username
        form['pwd'] = password
        response = s.post('https://www.novelupdates.com/login/',data=form)
        if response.url == 'https://www.novelupdates.com/':
            print("Login Sucessful")
            reading_list = s.get('https://www.novelupdates.com/reading-list/')
            # reading_html = lxml.html.fromstring(reading_list.text)
            # table_entries = reading_html.xpath('//tbody/tr/td/a')
            return reading_list.text
        else:
            print("Error Unable to log on")
            obj = open("Error.html","w")
            obj.write(response.text)
    else:
        print("Failure to access login page")
        sys.exit()

def html_parse(html):
    titles = []
    current_chapters = []
    latest_chapters = []
    soup = BeautifulSoup(html,'html.parser')
    print("Parsing Reading List")
    title_names = soup.find_all("tr",attrs={"class":"rl_links"})
    chapters = soup.find_all("a",attrs={"class":"chp-release"})
    counter = 0;
    if (len(chapters)%2) != 0:
        print("Error: Incorrect number of chapters")
        sys.exit()
    for i in range(len(title_names)):
        titles.append(title_names[i].attrs["data-title"])
        current_chapters.append(chapters[i + counter].get_text())
        latest_chapters.append(chapters[i+ counter + 1].get_text())
        counter += 1
    return(titles, current_chapters, latest_chapters)


def newChapters(titles, current_chapters, latest_chapters):
    num_of_books = len(titles)
    posted = []
    for i in range(num_of_books):
        if current_chapters[i] != latest_chapters[i]:
            posted.append(titles[i])
    if len(posted) != 0:
        if len(posted) > 1:
            print("New chapters have been posted for...")
        else:
            print("A new chapter has been posted for...")
        for post in posted:
            print("-    " + post)


html_string = scrapper()
titles, current_chapters, latest_chapters = html_parse(html_string)
newChapters(titles, current_chapters, latest_chapters)
