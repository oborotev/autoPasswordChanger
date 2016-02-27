#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
import datetime
import traceback
import getpass
import pause

# Change password func


def changePassword():
    ul_element = driver.find_element_by_class_name("nav-userinfo")
    li_element = ul_element.find_element_by_class_name("user-profile")
    li_element.find_element_by_xpath(
        "//a[@data-toggle='dropdown'][@href='#']").click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "open"))
    )
    ul_element = driver.find_element_by_class_name("user-profile-menu")
    ul_element.find_element_by_tag_name("a").click()
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "modal-title"))
    )
    driver.find_element_by_id("oldpassword").send_keys(USERNAME)
    driver.find_element_by_id("newpassword").send_keys(PASSWORD)
    driver.find_element_by_id("confirmpassword").send_keys(PASSWORD)
    driver.find_element_by_id("modal-confirm").click()
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "toast-message"))
    )

# Logger format config
LOGGER_FORMAT = '[%(asctime)-15s] %(levelname)s: %(message)s'

logging.basicConfig(
    format=LOGGER_FORMAT,
    level=logging.INFO,
    datefmt='%m/%d/%Y %I:%M:%S %p')

logging.info("Welcome to the autoPasswordChanger my friend")

USERNAME = input("Enter your Passport Number : ")
PASSWORD = getpass.getpass("Enter your Password (hidden in input) : ")
PAUSING = input("Do you want to wait for 7:30AM ? (yes or no) ")

# Check if password changed
password_changed = False

# Waiting for the date
if (PAUSING == "yes"):
    logging.info("Waiting for 2016-02-28 7:30AM...")
    pause.until(datetime.datetime(2016, 2, 28, 7, 30))

logging.info("autoPasswordChanger for coursechoose.bjtu.edu.cn v1.0")


logging.info("Waiting for system initialization...")
while (not password_changed):
    try:
        logging.info("PhantomJS driver initialization")
        driver = webdriver.PhantomJS()

        logging.info(
            "Setting window size to bigger size because responsivness in China is None...")
        driver.set_window_size(1000, 1000)

        logging.info("Retrieving http://coursechoose.bjtu.edu.cn ...")
        driver.get("http://coursechoose.bjtu.edu.cn/")
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        logging.info("Writing the username and password...")
        login_form = driver.find_element_by_id('login')
        login_form.find_element_by_name('username').send_keys(USERNAME)
        login_form.find_element_by_name('passwd').send_keys(USERNAME)

        logging.info("Sending the data...")
        driver.find_element_by_class_name('btn-turquoise').click()

        logging.info("Testing if we're connected...")
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "user-profile"))
        )
        logging.info("YOU ARE CONNECTED")
        logging.info("THESE MOTHERFUCKERS CHANGED THE PASSWORD!")
        logging.info("Changing the password...")
        changePassword()
        logging.info("Password successfully changed...")
        logging.info("Closing the driver...")
        driver.quit()
        logging.info("Password is safe my friend!")
        password_changed = True
    except Exception:
        logging.info("YOU ARE NOT CONNECTED")
        logging.info("IT IS STILL SAFE!")
        logging.info("Closing the driver...")
        driver.quit()
