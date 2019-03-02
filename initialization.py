from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from random import randint
from datetime import datetime
import csv
import json
import ast


class random():
    def rand_p(self):
        pilist = []
        with open('C:/Users/alexander/PycharmProjects/csvs/newpi.csv', 'r') as userfile:
            userfilereader = csv.reader(userfile)
            for col in userfilereader:
                pilist.append(col)

        pilist = ast.literal_eval(str(pilist[0]))

        userfile.close()

        prm = [181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 431, 433, 439, 733, 739,
               743,
               233, 257, 277, 827, 907, 941, 947, 953, 967, 971, 977, 983]

        item1 = randint(0, 9000)
        item2 = randint(9001, 20000)
        item3 = randint(20001, 30000)
        item4 = randint(30001, 39000)
        item5 = randint(39001, 48000)

        item11 = randint(0, 9000)
        item21 = randint(9001, 20000)
        item31 = randint(20001, 30000)
        item41 = randint(30001, 39000)
        item51 = randint(39001, 48000)

        # --------------------------------
        sepc = '.'
        rn = datetime.now()
        rn = str(rn)
        rn = rn.split(sepc, 1)[1]
        rn2 = int(rn) % 10
        if rn2 == 0 or rn2 > 12:  #
            while rn2 == 0 or rn2 > 12:
                sepc = '.'
                rn = datetime.now()
                rn = str(rn)
                rn = int(rn.split(sepc, 1)[1])
                rn2 = rn % 10

        if rn2 == 1:
            sd = randint(1, 20)
            sd = rn2 + sd
            p1 = int(prm[sd])
        elif rn2 == 34:
            sd = randint(1, 20)
            sd = rn2 - sd
            p1 = int(prm[sd])
        else:
            sd = rn2 + 1
            p1 = int(prm[sd])

        p = (int(pilist[item1]) * 10000 + int(pilist[item2]) * 1000 + int(pilist[item3]) * 100 + int(
            pilist[item4]) * 10 + int(pilist[item5]))
        q = (int(pilist[item51]) * 10000 + int(pilist[item41]) * 1000 + int(pilist[item31]) * 100 + int(
            pilist[item21]) * 10 + int(pilist[item11]))

        y = (p + 3 * q) % p1
        y = y ** 2

        y_list = list(str(y))
        y_1 = []
        for i in y_list:
            temp = int(i)
            y_1.append(temp)
        if len(y_1) >= 2:
            temp_list = []
            temp_list.append(y_1[0])
            pr = len(y_1) - 1
            t = randint(0, pr)
            temp_list.append(y_1[t])
            y_1 = temp_list[0] * 10 + temp_list[1]
        else:
            y_1 = y_1[0]
        return y_1

class actions():
    def mousemovements(self, driver):
        mv = ActionChains(driver)
        for mouse_x, mouse_y in zip(x_i, y_i):
            mv.move_by_offset(mouse_x, mouse_y)  # Random mosemovements using splines
            mv.perform()

    def scroll_end(self, driver):
        driver.find_element_by_tag_name('body').send_keys(
            Keys.END)  # Scroll with end so that i wont use js after the page has loaded

    def scroll_up(self, driver):
        driver.find_element_by_tag_name('body').send_keys(
            Keys.UP)

    def scroll_down(self, driver):
        driver.find_element_by_tag_name('body').send_keys(
            Keys.PAGE_DOWN)  # Scroll with end so that i wont use js after the page has loaded


def send(driver, cmd, params={}):
    resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
    url = driver.command_executor._url + resource
    body = json.dumps({'cmd': cmd, 'params': params})
    response = driver.command_executor._request('POST', url, body)
    if response['status']:
        raise Exception(response.get('value'))
    return response.get('value')


def add_script(driver, script):
    send(driver, "Page.addScriptToEvaluateOnNewDocument", {"source": script})  # adding js to the driver so that i can hide that it is a webdriver and that it is in headless mode


def initialize():

    x = randint(1480, 1536)
    y = randint(724, 864)
    argmnt = 'window-size='+str(x)+','+str(y)
    opts = Options()
    opts.add_argument(argmnt)
    # opts.add_argument('headless')
    # opts.add_argument('--disable-webrtc-multiple-routes')
    opts.add_argument('--ignore-certificate-errors')
    # opts.add_argument("--incognito")
    opts.add_argument("--start-maximized")
    opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36")
    prefs = {'profile.default_content_setting_values.notifications': 2}
    opts.add_experimental_option('prefs', prefs)
    opts.add_argument('start-maximized')

    #xy = proxy
    #opts.add_argument(xy)

    driver = webdriver.Chrome("C:/Users/alexander/PycharmProjects/chromedriver_win32/chromedriver.exe",  chrome_options=opts)

    WebDriver.add_script = add_script
    driver.add_script("Object.defineProperty(navigator, 'webdriver', {get: () => false,});")  # initializing the driver
    driver.add_script("window.chrome = { runtime: {} };")
    driver.add_script(
        "window.navigator.permissions.query = (parameters) => ( parameters.name === 'notifications' ? Promise.resolve({ state: Notification.permission }) : originalQuery(parameters) );")
    driver.add_script("Object.defineProperty(navigator, 'plugins', {  get: () => [1, 2, 3, 4, 5], });")
    driver.add_script(
        "WebGLRenderingContext.prototype.getParameter = function(parameter) { if (parameter === 37445) { return 'Intel Open Source Technology Center'; } if (parameter === 37446) { return 'ANGLE (Intel(R) HD Graphics 520 Direct3D11 vs_5_0 ps_5_0)'; }};")

    return driver
