from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

#Path de chromedriver
path = '/home/danel149/chromedriver'

service = Service()
#Opciones de chrome
options = webdriver.ChromeOptions()
##Estas linea solo para trabajar desde pdvsa
#options.add_argument('--disable-extensions')
#proxy = "10.172.31.3:8000"
#options.add_argument('--proxy-server=%s' % proxy)

driver = webdriver.Chrome(service=service, options=options)

#Iniciar el navegador
driver.get('https://buy2race.com/es/')

moto='Yamaha XTZ 700 TENERE'
buscarmoto = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="search_widget"]/form/input[2]')))
buscarmoto.send_keys(moto)