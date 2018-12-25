from dotenv import load_dotenv
import os
import getpass

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir,'.env'))

class Settings():
    def __init__(self):
        self.prompt = "prompt" in os.environ
        self.offload = "offload" in os.environ
        self.username = os.environ.get("username")
        self.password = os.environ.get("password")
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
            userInput = input("Enter your NovelUpdate username: ")
            configFile.write("username = " + userInput + "\n")
            self.username = userInput
            userInput = getpass.getpass("Enter your NovelUpdate password: ")
            configFile.write("password = " + userInput+ "\n")
            self.password = userInput
            configFile.close()
            return self.username, self.password
        else:
            return None, None
