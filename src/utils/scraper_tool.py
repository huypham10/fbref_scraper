#import packages
from selenium import webdriver as wb
import pandas as pd
import numpy as np
import urllib.request
import os
import time
import random
import re
from urllib.error import HTTPError



from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def open_chrome_window(url='https://google.com', proxy=False, headless=False,chromedriver_path="C:\\Users\\Huy's\\Downloads\\chromedriver.exe"):
	"""
	Launch new instance of webdriver using chromedriver. Returns the webdriver instance.
	"""

	from selenium.webdriver.chrome.options import Options

	assert type(proxy) == bool and type(headless) == bool, 'proxy and headless variables must be either True or False'
	assert not (proxy==True & headless==True), 'proxy chromedriver does not allow to be run headless'
	
	chrome_options = Options()

	if proxy:
		chrome_options.add_extension("C:\\Users\\Huy's\\Downloads\\ultrasurf.crx")
	if headless:
		chrome_options.add_argument("--headless")

	ua = UserAgent()
	userAgent = ua.random
	chrome_options.add_argument(f'user-agent={userAgent}')
	wbD = wb.Chrome(service=Service(chromedriver_path),
					options=chrome_options)
	
	wbD.get(url)
	# if proxy: #turn off ultrasurf tab
	# 	WebDriverWait(wbD, 10).until(EC.number_of_windows_to_be(2))
	# 	wbD.switch_to.window(wbD.window_handles[1])
	# 	wbD.close()
	# 	wbD.switch_to.window(wbD.window_handles[0])

	return wbD

def open_new_tab(url, driver, wait_time=4):
	"""
	Opens a new tab on the specified webdriver and wait for a specified number of seconds for the page to load. Need to call close current tab after finishing with the tab.
	"""
	assert type(wait_time) == int, 'variable wait_time needs to be an integer'
	prev_handles = driver.window_handles
	driver.execute_script(f"window.open('{url}')")
	WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(len(prev_handles)+1))
	curr_handles = driver.window_handles
	new_tab = [i for i in curr_handles if i not in prev_handles]
	
	driver.switch_to.window(new_tab[0])
	time.sleep(random.randint(wait_time-2,wait_time+2))

def close_current_tab(driver):
	"""
	Close the current tab and switch to the previous tab on the specified webdriver.
	"""
	curr_handles = driver.window_handles
	assert len(curr_handles)>1, 'Only works with multiple tabs windows. If you want to close the entire driver window call driver.quit() instead.'
	curr_handles.remove(driver.current_window_handle)
	driver.close()
	driver.switch_to.window(curr_handles[-1])