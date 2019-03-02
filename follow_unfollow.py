from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from initialization import initialize
from selenium.webdriver.common.by import By
from initialization import random
from random import randint
from initialization import actions
from random import uniform
import csv
import time
import pickle


def login(driver):
    username = '380988405753'
    password = 'A1234567890!!s'
    r = random()
    time.sleep(r.rand_p())

    elmnt = driver.find_element_by_xpath('//*[@id="email"]')  # Finds the username
    elmnt1 = driver.find_element_by_xpath('//*[@id="pass"]')  # Finds the password

    for char1 in username:
        elmnt.send_keys(char1)
        t = (r.rand_p() % 10) / 10
        t1 = uniform(0.1, t)
        time.sleep(t1)  # pause for 0.X seconds

    for char2 in password:
        elmnt1.send_keys(char2)
        t = (r.rand_p() % 10) / 10
        t1 = uniform(0.1, t)
        time.sleep(t1)  # pause for 0.X seconds

    z = r.rand_p()
    z = z % 10
    print(z)
    time.sleep(z)

    while True:
        try:
            driver.find_element_by_id('loginbutton').click()  # clicks the login button
            print('Succesfully Logged in')
            break
        except:
            pass


def current_user(friend):
    c_user = open('c_follow.txt', 'a', encoding='utf8')
    c_user.write(friend + '\n\n\n')
    c_user.close()


def today_f():
    follow_list = []

    with open('follow.txt', 'r',
              encoding="utf8") as userfile:
        csvreader = csv.reader(userfile)

        for line in csvreader:
            follow_list.append(str(line[0]))
    print('the actual unique list length is ', len(follow_list))
    userfile.close()
    return follow_list


def today_unf(friend):
    c_user = open('followed.txt', 'a', encoding='utf8')
    c_user.write(friend + '\n')
    c_user.close()


def all_crawled(friend):
    c_user = open('followed.txt', 'a', encoding='utf8')
    c_user.write(friend + '\n')
    c_user.close()


def visit(driver):
    r = random()
    print('Visit page')
    driver.get("https://instagram.com")
    z = r.rand_p()
    z1 = r.rand_p()
    if z > 10:
        z = z % 10
        z = z // 2
    print('will stay for ', z)
    for i in range(0, z):
        time.sleep(z1)
        print('this is the ', i)
        print('time staying is ', z1)
        action.scroll_down(driver)


def follow_spree(driver):

    r = random()

    follow_list = today_f()

    profiles_crawled = 1

    max_profiles = randint(40, 48)

    for follow in follow_list:

        current_user(follow)
        all_crawled(follow)
        today_unf(follow)

        print('\n\n\n')
        print('==================')
        print(follow)

        time.sleep(r.rand_p())
        if profiles_crawled > 1:
            visit(driver)

        follow_url = 'https://instagram.com/'+follow

        driver.get(follow_url)

        time.sleep(r.rand_p())
        counter = 1
        while True:
            try:
                driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/span/span[1]/button').click()
                break
            except:
                counter += 1
                if counter >= 10:
                    break
                time.sleep(1)
                pass

        time.sleep(r.rand_p())

        profiles_crawled += 1

        if profiles_crawled >= max_profiles:
            break


def save_cookies(driver):

    pickle.dump(driver.get_cookies(), open('cookies.txt', "wb"))
    print('cookies saved successfully')


def load_cookies(driver):

    cookies = pickle.load(open('cookies.txt', "rb"))
    driver.delete_all_cookies()
    # have to be on a page before you can add any cookies, any page - does not matter which
    driver.get("https://amazon.com")
    for cookie in cookies:
        driver.add_cookie(cookie)
    print('cookies loaded successfully')


if __name__ == '__main__':

    dr = initialize()
    action = actions()

    #load_cookies(dr)

    dr.get('https://instagram.com')

    time.sleep(50)

    follow_spree(dr)

    #unfollow_spree(dr)

    #save_cookies(dr)

    dr.quit()
