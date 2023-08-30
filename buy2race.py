from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import pandas as pd

import time


service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

#Iniciar el navegador
driver.get('https://buy2race.com/es/')

moto='Yamaha XTZ 700 TENERE'

buscador = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="search_widget"]/form/input[2]')))
buscador.click()#send_keys(moto)

buscarmoto = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="df-searchbox__dffullscreen"]')))
buscarmoto.send_keys(moto)

time.sleep(3)

    ## Datos a guardar
result = []
links = driver.find_elements(By.XPATH, '//div[@class="df-card"]/a')
titles = driver.find_elements(By.XPATH, '//div[@class="df-card__title"]')
availitys = driver.find_elements(By.XPATH, '//div[@class="df-card__pricing"]/span/span')
prices = driver.find_elements(By.XPATH, '//span[@class="df-card__price "]')


    # Añadir los valores a la lista de resultados
for i in range(len(links)):
    result.append({
        "Title": titles[i].text,
        "Availity": availitys[i].get_attribute("class"),
        "Price": prices[i].text,
        "Link": links[i].get_attribute("href")
    })

# Crear el dataframe
df = pd.DataFrame(result)
df.to_csv('ymaha_xtz_700_tenere_raw.csv', index=False)
print(df)
