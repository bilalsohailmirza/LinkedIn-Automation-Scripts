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

url = "https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH&page="


for i in range(5):
    # navigating to the connections page
    driver.get(url+str(i+1))
    time.sleep(5)

    # getting all buttons on the people page
    all_buttons = driver.find_elements_by_tag_name("button")
    message_buttons = [btn for btn in all_buttons if btn.text == "Message"]

    # getting all the spans on the page
    all_spans = driver.find_elements_by_tag_name("span")
    all_spans = [s for s in all_spans if s.get_attribute("aria-hidden") == "true"]

    idx = [*range(12, 49, 4)]
    names_list = []

    for k in idx:
        name = all_spans[k].text.split()[0]
        names_list.append(name)   

    print(names_list)

    for j in range(len(message_buttons)):

        message_buttons[j].click()
        time.sleep(3)

        # all_buttons = driver.find_elements_by_tag_name("button")

        # now selecting message box div
        message_box_div = driver.find_element_by_xpath("//div[starts-with(@class, 'msg-form__msg-content-container')]")
        # message_box_div.click()
        time.sleep(1)
        # selecting message paragraph
        paragraphs = driver.find_elements_by_tag_name("p")

        message = f"Hey {names_list[j]}! Did not mean to bother you. This message is from a bot. Kindly ignore this message."
        try:
            # if paragrpahs[-5].text != "":
            #     paragrpahs[-5].send_keys(Keys.CONTROL + "a")
            #     paragrpahs[-5].send_keys(Keys.BACK_SPACE)
                
            # time.sleep(2)
            paragraphs[-5].send_keys(message)
            time.sleep(2)
            all_buttons = driver.find_elements_by_tag_name("button")

            # send_button = [btn for btn in all_buttons if btn.text == "Send"]
            # send_button[0].click()
            time.sleep(2)
        except:
            print("Skipping a Contact")
        #     continue
        
        # selecting chat closing button
        time.sleep(2)
        all_buttons = driver.find_elements_by_tag_name("button")
        close_button = [btn for btn in all_buttons if btn.text[:10] == "Close your"]
        close_button = close_button[0]
        close_button.click()

        all_buttons = driver.find_elements_by_tag_name("button")
        discard_buttons = [btn for btn in all_buttons if btn.text == "Discard"]
        discard_buttons[0].click()

