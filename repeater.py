import os
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

class Repeater:
    def __init__(self):
        self.TARGET =  str(input("enter url:\n")) #None #add target from tk input
        self.target_activity = None
        self.webdriver_options = FirefoxOptions()
        self.webdriver_options.add_argument("--headless")
        self.webdriver = webdriver.Firefox(options=self.webdriver_options)

        while self.target_activity != True:
            try:
                if requests.get(self.TARGET).status_code == 200:
                    self.target_activity = True
                else:
                    print("The host is not responding, it maybe down/blocked in your area ")
            except Exception as e:
                print("That url seems wrong!, please try again")

    def set_cookie(self,cookie_name,cookie_value):
        self.cookie_name = cookie_name
        self.cookie_value = cookie_value
        self.webdriver.add_cookie({"name": self.cookie_name, "value": self.cookie_value})
        print("Cookie added to current session:\n",self.webdriver.get_cookie(self.cookie_name))

    def repeat_request(self,payload_file,request_string):
        self.rep_request = request_string
        self.payload_file = payload_file
        with open(self.payload_file,"r+") as payload_file:
            for payload in payload_file:
                curr_payload = self.rep_request.replace("BREAKPOINT", payload)



repeater = Repeater()

#####################################
