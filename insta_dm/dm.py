from config import info
import time
import logging
from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.firefox.options import Options


options = Options()
options.headless = True
Path = info.path
user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", user_agent)
driver = webdriver.Firefox(profile, executable_path=Path, options=options)
driver.set_window_size(360,640)

wait = WebDriverWait(driver, 90)

def wait_until(string):
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f'{string}')))

usernames = info.usernames

def main():
    driver.get('https://instagram.com/')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.L3NKy')))
    login_button = driver.find_element_by_css_selector('.L3NKy').click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.Et89U:nth-child(4) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')))
    username = driver.find_element_by_css_selector('div.Et89U:nth-child(4) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
    username.send_keys(info.username)
    password = driver.find_element_by_css_selector('div.Et89U:nth-child(5) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
    password.send_keys(info.password)
    password.send_keys(Keys.RETURN)
    time.sleep(1)
    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'olLwo')))
        click = driver.find_element_by_css_selector('button.sqdOP:nth-child(1)').click()
    except Exception as e:
        logging.exception('no save ask')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xWeGp > svg:nth-child(1)')))
    message_button = driver.find_element_by_css_selector('.xWeGp > svg:nth-child(1)').click()
    wait_until('button.yWX7d:nth-child(1)')
    driver.find_element_by_css_selector('button.yWX7d:nth-child(1)').click()
    wait_until('.wpO6b > svg:nth-child(1)')
    driver.find_element_by_css_selector('.wpO6b > svg:nth-child(1)').click()
    for names in usernames:
        wait_until('.K3Sf1')
        search_bar = driver.find_element_by_css_selector('.j_2Hd')
        search_bar.send_keys(names)
        time.sleep(.1)
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div[2]/div/div[2]/div/div/div[3]/button/span')))
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[1]/section/div[2]/div/div[2]/div/div/div[3]/button/span').click()
        wait_until('.cB_4K')
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/div[1]/header/div/div[2]/button')))
        driver.find_element_by_xpath('/html/body/div[1]/section/div[1]/header/div/div[2]/button').click()
        wait_until('.ItkAi > textarea:nth-child(1)')
        driver.find_element_by_css_selector('.ItkAi > textarea:nth-child(1)').send_keys(info.message)
        driver.find_element_by_css_selector('div.JI_ht:nth-child(2) > button:nth-child(1)').click()
        driver.find_element_by_css_selector('.Iazdo > span:nth-child(1) > svg:nth-child(1)').click()
        time.sleep(randint(1,5))
    driver.close()
    print('done')
    quit()

if __name__ == "__main__":
    main()