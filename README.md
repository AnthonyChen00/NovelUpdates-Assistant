# NovelUpdate Assistant
## Summary
This project is to create an assistant to navigate through the popular web novel forum/website, [NovelUpdates](https://www.novelupdates.com)(NU), without actually browsing/reading through the website. Most of these web novels originate from Asia (mainly China, Korea, and Japan), and people translate them so more people can enjoy reading these novels. NU is one of the best resources for readers to check whether or not a new chapter has been translated for their favorite novels. Users of the website can add novels to a "reading list", a way to consolidate all the different novels and their latest chapters. I frequently browse this website to check if new updates have been released or for a new novel read. To learn and practice web scraping, I designed a program to quickly check whether a new novel has been updated without the need to browse the website. There are other ideas I have been planning on adding onto this.

## Setting up:
To ensure that all the necessary Python libraries for the main script are installed
```bash
pip install -r requirements.txt
```

## Running code:
The current main program function is to determine whether or not there are new chapters posted for the user's reading list. User login credentials are required for the program to access the reading list. At the initial launch program will prompt a few features that the user may want to use such as, saving credentials locally rather than entering every time or having the program enter a state where it periodically follows a set schedule to see if there is a new update rather than running the program every time.
```bash
$ python3 NU_Scraper.py
Do you want to use save file (y/n): y
Enter your NovelUpdate username:
Enter your NovelUpdate password:
WIP: will add functions to read based of files
	  ===Login Sucess===
	 Parsing Reading List
 ====================================
There are 3 new updates...
 0 - Against the Gods
 1 - Heavenly Jewel Change
 2 - Overgeared
```
## Settings:
At the initial launch, the script will prompt several questions regarding using features like saving credentials on a local file or having the program enter a state of scheduled checks for new updates. The options for these features are saved within a file ".env" within the current directory of the program.
### Scheduled Checks
 The scheduled updates uses two additional values, one for how long the script waits until checking the website and one for which hours the program checks. These two values can be modified within "settings.py". The current configuration is that the program will wait an hour before checking the time, and if the current hour is 8am, 12pm, or 4pm, the program will check if there are new updates. Simply closing the program or ctrl+c to end the schedule checks

## Goals:
* adding a method of launching the latest chapter on preferred web browser to the latest chapter or maybe the next chapter to about to reading
* scraping the chapter text and ignoring the ads *(skeptical since ad revenue helps the translators)*
* ~~creating and updating a user file within the local machine with data rather than pulling data from website at each launch of script~~
* porting to raspberry pi to running continuously and notify when new chapters are posted
* ~~scheduled logins to check if new chapters have been posted~~
