from selenium import webdriver
import random
import sys
import time

target = sys.argv[1]
google_url = "https://www.google.com/search?num=25&q=site%3A"+target+"+filetype%3Ajsp+OR+filetype%3Aphp+OR+filetype%3Aasp+OR+filetype%3Aaspx"


page = 0
while page < 1000:
    driver = webdriver.Chrome('./chromedriver')
    driver.get(google_url + "&start="+str(page))
    if "continue" in driver.current_url or "sorry/index" in driver.current_url:
        print("please resolve captcha...type something when you finished")
        while not input():
            continue

    print("captcha resolved! Congratulations, you are not a robot! (maybe) :)")        
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        url = elem.get_attribute("href")
        if target in url and "google.com" not in url:
            print(url)
    page = page + 10
    driver.close()
    sleep_time = random.randint(10,25)
    print("resuming session in " + str(sleep_time)+"...")
    time.sleep(sleep_time)


