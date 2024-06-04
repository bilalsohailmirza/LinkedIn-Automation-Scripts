
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
driver.get('https://linkedin.com/login')


time.sleep(2)

username = driver.find_element_by_xpath('//input[@name="session_key"]')
password = driver.find_element_by_xpath('//input[@name="session_password"]')

username.send_keys('')
password.send_keys('')

time.sleep(2)

submit = driver.find_element_by_xpath('//button[@type="submit"]')
submit.click()



# pressing enter on empty search bar search bar 
time.sleep(3)
serach_bar = driver.find_element_by_xpath('//input[@placeholder="Search"]')
serach_bar.send_keys(Keys.ENTER)


# now clicking on people's button
time.sleep(5)
all_buttons = driver.find_elements_by_tag_name("button")
people_button = [btn for btn in all_buttons if btn.text == "People"]
people_button = people_button[0]
people_button.click()


# now clicking on first connection button
time.sleep(5)
all_buttons = driver.find_elements_by_tag_name("button")
first_button = [btn for btn in all_buttons if btn.text == "1st"]
first_button = first_button[0]
first_button.click()


# Now clicking on Message Button

time.sleep(5)
all_buttons = driver.find_elements_by_tag_name("button")
message_buttons = [btn for btn in all_buttons if btn.text == "Message"]



for i in range(1,3):

    message_buttons[i].click()
    time.sleep(3)

    # all_buttons = driver.find_elements_by_tag_name("button")

    # now selecting message box div
    message_box_div = driver.find_element_by_xpath("//div[starts-with(@class, 'msg-form__msg-content-container')]")
    message_box_div.click()
    time.sleep(1)
    # selecting message paragraph
    paragrpahs = driver.find_elements_by_tag_name("p")
    message = "Did not mean to bother you. This message is from a bot. Kindly ignore this message."
    try:
        if paragrpahs[-5].text != "":
            paragrpahs[-5].send_keys(Keys.CONTROL + "a")
            paragrpahs[-5].send_keys(Keys.BACK_SPACE)
            time.sleep(2)
        paragrpahs[-5].send_keys(message)

        all_buttons = driver.find_elements_by_tag_name("button")

        send_button = [btn for btn in all_buttons if btn.text == "Send"]
        send_button[0].click()
        time.sleep(2)
    except:
        continue
    
    # selecting chat closing button
    all_buttons = driver.find_elements_by_tag_name("button")
    close_button = [btn for btn in all_buttons if btn.text[:28] == "Close your conversation with"]
    close_button = close_button[0]
    close_button.click()





