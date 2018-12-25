# NovelUpdate Assistant
## Summary
This project is to create an assistant to navigate through the popular web novel,  forum/website, [NovelUpdates](https://www.novelupdates.com)(NU), without actually browsing/reading through the website. Most of these web novels originate from Asia (mainly China, Korea, and Japan), and people translate them so more people can enjoy reading these novels. NU is one of the best resources for readers to check whether or not a new chapter has been translated for their favorite novels. Users of the website can add novels to a "reading list", a way to consolidate all the different novels and their latest chapters. I frequently browse this website to check if new updates have been released or for a new novel read. To learn and practice web scraping, I designed a program to quickly check whether a new novel has been updated without the need to browse the website. There are other ideas I have been planning on adding onto this.

## Setting up:
To ensure that all the necessary Python libraries for the main script are installed
*Skip the setup if you are using the virtual environment within this repo*
```bash
pip install -r requirements.txt
```
Or launch the virtual environment
```bash
source venv/bin/activate
```

## Running code:
The current main program function is to determine whether or not there are new chapters posted for the user's reading list. User login credentials are required for the program to access the reading list. Currently the login information is not stored anywhere within the program, but rather asked in the beginning of the script
```bash
$ python3 NU_Scraper.py
Enter your NovelUpdates Username: 
Enter your NovelUpdates Password:
Login Sucessful
Parsing Reading List
New chapters have been posted for...
-    Against the Gods
-    Heavenly Jewel Change
-    Overgeared
```

## Goals:
* adding a method of launching the latest chapter on preferred web browser to the latest chapter or maybe the next chapter to about to reading
* scraping the chapter text and ignoring the ads *(skeptical since ad revenue helps the translators)*
* creating and updating a user file within the local machine with data rather than pulling data from website at each launch of script
* porting to raspberry pi to running continuously and notify when new chapters are posted
