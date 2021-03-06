from dotenv import load_dotenv
import os
import getpass

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir,'.env'))

class Settings():
    def __init__(self):
        self.prompt = "prompt" in os.environ
        self.offload = "offload" in os.environ
        self.scheduled = "scheduled" in os.environ
        self.username = os.environ.get("username")
        self.password = os.environ.get("password")
        self.time = ['8','12','16'] #the hours (24) the program will check
        self.pause = 3600 #number of seconds at each pause
        if os.path.isfile(".env") == False:
            obj = open(".env","x")
            obj.close()

    def initialization(self):
        userInput = ""
        configFile = open(".env","a")
        configFile.write("prompt = True\n")
        userInput = input("Do you want to use save file (y/n): ")
        while(userInput != "n" and userInput != "y"):
                    userInput = input("Do you want to use save file (y/n): ")
        if (userInput == "y"):
            configFile.write("offload = True\n")
            userInput = input("Do you wish use the scheduled login to check for chapters daily (y/n): ")
            while(userInput != "n" and userInput != "y"):
                        userInput = input("Do you wish use the scheduled login to check for chapters daily (y/n): ")
            if userInput == "y":
                configFile.write("scheduled = True\n")
                self.scheduled = True
            userInput = input("Enter your NovelUpdate username: ")
            configFile.write("username = " + userInput + "\n")
            self.username = userInput
            userInput = getpass.getpass("Enter your NovelUpdate password: ")
            configFile.write("password = " + userInput+ "\n")
            self.password = userInput
            configFile.close()
            if os.path.isfile("readingList.txt") == False:
                readingFile = open("readingList.txt","x")
                readingFile.close()
            return self.username, self.password
        else:
            return None, None
