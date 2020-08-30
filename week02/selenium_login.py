from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    
    browser.get('https://shimo.im/welcome')
    time.sleep(1)

    browser.find_element_by_xpath('//*[@class="login-button btn_hover_style_8"]').click()

    browser.find_element_by_xpath('//*[@name="mobileOrEmail"]').send_keys('13428776757')
    browser.find_element_by_xpath('//*[@name="password"]').send_keys('test123')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@class="sm-button submit sc-1n784rm-0 bcuuIb"]').click()

    cookies = browser.get_cookies()
    print(cookies)
    time.sleep(3)

except Exception as e:
    print(e)

finally:
    browser.close()