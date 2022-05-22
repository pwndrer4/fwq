from selenium import webdriver
import time
import random
import os
browser=webdriver.PhantomJS(executable_path="./phantomjs/bin/phantomjs")
browser.implicitly_wait(30)
browser.get("https://accounts.goorm.io/login?return_url=aHR0cHM6Ly9pZGUuZ29vcm0uaW8vbXkvZGFzaGJvYXJkP3JlZGlyZWN0PTE=") 
browser.set_window_size(1920,1080)                                        
browser.find_element_by_name("email").send_keys(os.environ["USERNAME"])
browser.find_element_by_name("password").send_keys(os.environ["PASSWORD"])
browser.find_element_by_class("btn-primary").click()                               
browser.find_element_by_class("btn-outline-primary").click()              
while True:
    browser.execute(webdriver.remote.command.Command.MOVE_TO,{
        "xoffset":random.randint(0,1920),
        "yoffset":random.randint(0,1080)
    })                                                                    
    time.sleep(random.randint(0,10))
