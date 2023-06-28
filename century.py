from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
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
driver.get('https://www.century21.com.ve/')

#todos el inventario '//div[@class="all-listings-wrapper"]/a/text()'
inventario = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//div[@class="all-listings-wrapper"]/a')))
inventario.click() #.sendkeys('madrid')

#label pais'//*[@id="filterSidebar"]/div/div[2]/fieldset[2]/div[2]/div/button'
pais = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="filterSidebar"]/div/div[2]/fieldset[2]/div[2]/div/button')))
pais.click() #.sendkeys('madrid')

#Check box venezuela: 
#react-select-13-option-0 > input[type=checkbox] 
check = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.CSS_SELECTOR,'#react-select-13-option-0 > input[type=checkbox]')))
check.click() 

#boton del estado /html/body/div[2]/div/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/fieldset[3]/div[2]/div/button
estatebutton = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/fieldset[3]/div[2]/div/button')))
estatebutton.click() 

#anzoategui /html/body/div[2]/div/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/fieldset[3]/div[2]/div/div[1]/div/div[2]/div/div[2]
anzoategui = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/fieldset[3]/div[2]/div/div[1]/div/div[2]/div/div[2]')))
anzoategui.click() 

#label ciudad /html/body/div[2]/div/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/fieldset[4]/div[2]/div/button
citybutton = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/fieldset[4]/div[2]/div/button')))
citybutton.click()

#lecheria /html/body/div[2]/div/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/fieldset[4]/div[2]/div/div[1]/div/div[2]/div/div[20]/input
lecheria =driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/fieldset[4]/div[2]/div/div[1]/div/div[2]/div/div[20]/input')
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)",lecheria)
lecheria.click()

time.sleep(5)

## Datos a guardar
## Total de resultados  /html/body/div[2]/div/div/div/main/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/h5


tipo = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[2]/div/div[1]/div[2]/div[1]').text
tipovivienda = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[2]/div/div[1]/div[2]/a').text
precio = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[2]/div/div[1]/div[2]/div[5]').text
ubicacion = driver.find_element(By.CSS_SELECTOR, '#main > div.row.mt-4 > div:nth-child(2) > div > div.d-flex.flex-wrap.flex-xxl-nowrap.justify-content-center > div.flex-grow-1.d-flex.flex-column.bd-highlight.mb-3.position-relative > div.text-muted.font-weight-light.text-truncate.small.m-0').text
terreno = driver.find_element(By.CSS_SELECTOR,'#main > div.row.mt-4 > div:nth-child(2) > div > div.d-flex.flex-wrap.flex-xxl-nowrap.justify-content-center > div.flex-grow-1.d-flex.flex-column.bd-highlight.mb-3.position-relative > div.mt-2.text-muteds.text-truncate.small > span:nth-child(1) > span').text
construccion = driver.find_element(By.CSS_SELECTOR,'#main > div.row.mt-4 > div:nth-child(2) > div > div.d-flex.flex-wrap.flex-xxl-nowrap.justify-content-center > div.flex-grow-1.d-flex.flex-column.bd-highlight.mb-3.position-relative > div.mt-2.text-muteds.text-truncate.small > span:nth-child(3) > span').text
habitaciones = driver.find_element(By.XPATH,'//*[@id="main"]/div[2]/div[2]/div/div[1]/div[2]/div[4]/span[1]').text
banos = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[2]/div/div[1]/div[2]/div[4]/span[2]').text
estacionamientos = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[2]/div/div[1]/div[2]/div[4]/span[3]').text
link = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[2]/div/div[1]/div[2]/div[6]/div/div/div[2]/a').get_attribute("href")
pool=driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[2]/div/div[1]/div[2]/div[4]/span[4]').text
if pool == 'Piscina':
    pool=True
else:
    pool=False
print(tipo, tipovivienda, precio, 
      ubicacion, terreno, construccion, 
      habitaciones, banos, estacionamientos, 
      link, pool)
