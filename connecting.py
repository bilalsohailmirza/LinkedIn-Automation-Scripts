from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument(r"--user-data-dir=/home/username/.config/google-chrome")
options.add_argument(r'--user-profile=Default')

driver = webdriver.Chrome(options=options)
driver.get('https://linkedin.com/login')


# def SignIn():
time.sleep(2)

username_input = driver.find_element_by_xpath('//input[@name="session_key"]')
password_input = driver.find_element_by_xpath('//input[@name="session_password"]')

# reading email and password from file
file = open('credentials.txt','r')
email = file.readline()
password = file.readline()
file.close()

username_input.send_keys(email)
password_input.send_keys(password)


time.sleep(2)

submit = driver.find_element_by_xpath('//button[@type="submit"]')
submit.click()



url_2nd = "https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page="

url_3rd = "https://www.linkedin.com/search/results/people/?network=%5B%22O%22%5D&origin=FACETED_SEARCH&page="


for i in range(5):
    # navigating to the connections page
    driver.get(url_2nd+str(i+1))
    time.sleep(5)

    # getting all buttons on the people page
    all_buttons = driver.find_elements_by_tag_name("button")
    connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

    # getting all the spans on the page
    all_spans = driver.find_elements_by_tag_name("span")
    all_spans = [s for s in all_spans if s.get_attribute("aria-hidden") == "true"]

    # counter = 0
    # for s in all_spans:
    #     print(counter)
    #     print(s.text)
    #     counter += 1

    idx = [*range(14, 51, 4)]
    names_list = []

    for k in idx:
        name = all_spans[k].text.split()[0]
        names_list.append(name)   

    print(names_list)

    for j in range(len(connect_buttons)):

        connect_buttons[j].click()
        time.sleep(2)

        all_buttons = driver.find_elements_by_tag_name("button")
        note_buttons = [btn for btn in all_buttons if btn.text == "Add a note"]
        note_buttons[0].click()
        time.sleep(2)
        message = f"Hey {names_list[j]}! I’ve noticed your presence here on LinkedIn, and I’m so impressed by your work! Would love to connect."

        text_area = driver.find_element_by_id("custom-message")
        text_area.send_keys(message)

        # --------- CLICKING ON THE SEND BUTTON ----------- 
        # all_buttons = driver.find_elements_by_tag_name("button")
        # submit_buttons = [btn for btn in all_buttons if btn.text == "Send"]
        # submit_buttons[0].click()
        time.sleep(2)


        # selecting chat closing button
        time.sleep(2)
        all_buttons = driver.find_elements_by_tag_name("button")
        close_button = [btn for btn in all_buttons if btn.get_attribute('aria-label') == "Dismiss"]
        close_button = close_button[0]
        close_button.click()

    time.sleep(2)


