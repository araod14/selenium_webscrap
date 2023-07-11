from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import pandas as pd
import time

#Path de chromedriver
path = '/home/danel149/chromedriver'

#Opciones de chrome
options = webdriver.ChromeOptions()
##Estas linea solo para trabajar desde pdvsa
#options.add_argument('--disable-extensions')
#proxy = "10.172.31.3:8000"
#options.add_argument('--proxy-server=%s' % proxy)

driver = webdriver.Chrome(path, chrome_options=options)

#Iniciar el navegador
driver.get('https://tuhome24.com.ve/')

# Clic selector de estado
estado = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="select_banner_estado"]')))
estado.click() #.sendkeys('madrid')

#Elige Anzoategui
anz = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="select_banner_estado"]/option[3]')))
anz.click() 

# clic boton zona
zonebutton = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="select_banner_zona"]')))
zonebutton.click()

# clic elegir lecheria
lecheria = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="select_banner_zona"]/option[25]')))
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)",lecheria)


#lecheria =driver.find_element(By.CSS_SELECTOR,'#select_banner_zona > option:nth-child(25)')
lecheria.click()

# clic boton zona
zonebutto = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="select_banner_zona"]')))
zonebutto.click()

# clic en buscar
busqueda = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'/html/body/section[2]/div[3]/form/div[2]/div/div[6]/div/button')))
busqueda.click()

time.sleep(5)

listasdepaginas = driver.find_elements(By.XPATH,'//div[@class="pagination"]/ul[@class="pagination"]/li')

def info():
    casas = driver.find_elements(By.XPATH, '//div[@class="col-12 col-sm-6 col-md-6 col-lg-4 mt-3"]')
    vivi=[]
    for casa in casas:
        viviendas = driver.find_elements(By.XPATH, '//div[@class="col-12 col-sm-6 col-md-6 col-lg-4 mt-3"]')
        links = driver.find_elements(By.XPATH, '//div[@class="carousel-item active"]/a')
        vivi = [vivienda.text for vivienda in viviendas]
        links_to = [link.get_attribute("href") for link in links]
    return vivi

df = pd.DataFrame({"viviendas":info()})
#next = driver.find_element(By.XPATH, '//li[@class="page-item"]')

for i in range(3, 9):
#for i in range(6):
    page2 = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH, f'/html/body/form/div/div[3]/div[2]/div/div/ul/li[{i}]/a')))
    page2.click()

    df2 = pd.DataFrame({"viviendas":info()})
    df = pd.concat([df, df2], axis=0)

for i in range(10, 39):
    page9 = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH, '/html/body/form/div/div[3]/div[2]/div/div/ul/li[9]/a')))
    page9.click()
    df9 = pd.DataFrame({"viviendas":info()})
    df = pd.concat([df, df9], axis=0)


df.to_csv('viviendas_home24.csv', index=False)
print(df)
