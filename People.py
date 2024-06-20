from linkedin_scraper import Person, actions
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
driver = webdriver.Chrome()

file = open('credentials.txt','r')
email = file.readline()
password = file.readline()
file.close()

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument(r"--user-data-dir=/home/username/.config/google-chrome")
options.add_argument(r'--user-profile=Default')

actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person("https://www.linkedin.com/in/abdulalikazi/", driver=driver)