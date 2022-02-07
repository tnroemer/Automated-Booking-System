#!/usr/bin/env python
# coding: utf-8

# In[1]:

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import regex as re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
import sys
import os
import tqdm as tqdm
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
#pwinput


# In[ ]:


def log_in(name, passw):
    element = driver.find_element(By.ID, "userNameInput")
    element.clear()
    element.send_keys(name)
    element2 = driver.find_element(By.ID, "passwordInput")
    element2.clear()
    element2.send_keys(passw)
    element2.send_keys(Keys.RETURN)
    time.sleep(3)


# In[ ]:


def get_ids(signup):
    global singups
    if signup == 1:
        singups = ["Lunch: 11:45-13:30", "Lunch: 12:00-13:30"]
    elif signup == 2:
        signups = ["Low Table: 18:00-19:00"]
    elif signup == 3:
        signups = ["Lunch: 11:45-13:30", "Lunch: 12:00-13:30","Low Table: 18:00-19:00"]
    driver.get("https://meal.nuff.ox.ac.uk/Home/")
    try:
        elem = WebDriverWait(driver, 2).until(EC.title_contains("EBS - Events List"))
    finally:
        time.sleep(2)
        element = driver.find_elements(By.CSS_SELECTOR, "td:nth-child(3)")
        global event
        event = [e.text for e in element]
        element = driver.find_elements(By.CSS_SELECTOR, "td:nth-child(7) .btn-item-action")
        global ids
        ids = [int(re.findall("\d+",e.get_attribute("onclick"))[0]) for e in element]
        element = driver.find_elements(By.CSS_SELECTOR, "td:nth-child(2) .table-cell-content")
        global dates
        dates = [re.search(r'\d{2}/\d{2}/\d{2}', e.text).group() for e in element]
        condition = [e in signups for e in event]
        ids = [ids for ids,condition in zip(ids,condition) if condition == True]
        dates = [dates for dates,condition in zip(dates,condition) if condition == True]
        event = [event for event,condition in zip(event,condition) if condition == True]
        #df = pd.DataFrame(zip(dates,event,ids), columns=["Date","Event","ID"])
        #df = df[df['Event'].isin(signups)]
        #df.index = list(range(len(df)))


# In[ ]:


def sign_up(page, diet):
    driver.get("https://meal.nuff.ox.ac.uk/Booking/BookingPage/"+str(page))
    try:
        elem = WebDriverWait(driver, 2).until(EC.title_contains("EBS - Booking"))
    finally:
        time.sleep(2)
        element = driver.find_elements(By.CLASS_NAME, "inline-checkbox")
        if element[diet-1].is_selected() == False:
            element[diet-1].click()
    driver.find_element(By.CSS_SELECTOR, ".btn-form-action:nth-child(5)").click()


# In[ ]:


def resource_path(relative_path: str) -> str:
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


# In[ ]:


print("\n========================================\nWelcome to the Automated Booking System!\n========================================\n")
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(executable_path=os.path.join(os.path.dirname(__file__), "driver/chromedriver"), options=options)
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
actions = ActionChains(driver)


# In[ ]:


driver.get("https://intranet.nuff.ox.ac.uk/")


# In[ ]:


username = str(input("Username: "))
print("Note that the terminal will not show you any indicator for whether you typed anything or not for the password")
passw = getpass("Password: ")
signup = int(input("Which meals do you whish to sign up for?\n1: Lunch\n2: Dinner\n3: Both\n\n"))
print("")
diet = int(input("Dietary preference:\n1: NA\n2: Vegetarian\n3: Vegan\n4: No Red Meat\n5: Non Dairy\n6: Fruit Plate for Pudding\n7: Fish Eating Vegetarian\n8: No Pork\n9: No Shellfish\n10: Gluten Free\n\n"))
print("")


# In[ ]:


log_in(username,passw)


# In[ ]:


get_ids(signup)


# In[ ]:


pbar = tqdm.tqdm(total=len(ids))
for i in range(len(ids)):
    time.sleep(2.5)
    sign_up(ids[i],diet)
    pbar.write("Signed up for " + event[i].split(":",1)[0] + " on " + dates[i])
    pbar.update(1)
    
#for i in tqdm.tqdm(range(len(ids)), position=0, leave=True):
#    time.sleep(2.5)
#    sign_up(ids[i],diet)
#    print("Signed up for " + event[i].split(":",1)[0] + " on " + dates[i])


# In[ ]:


print("Thank you for using the Automated Booking System!")
driver.quit()


# In[ ]:


sys.exit()
