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

# Da click a todos los inventarios
inventario = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//div[@class="all-listings-wrapper"]/a')))
inventario.click() #.sendkeys('madrid')

# Clic selector de pais
pais = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="filterSidebar"]/div/div[2]/fieldset[2]/div[2]/div/button')))
pais.click() #.sendkeys('madrid')

#Elige venezuela
check = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.CSS_SELECTOR,'#react-select-13-option-0 > input[type=checkbox]')))
check.click() 

# clic boton del estado
estatebutton = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/fieldset[3]/div[2]/div/button')))
estatebutton.click() 

# clic elige anzoategui
anzoategui = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/fieldset[3]/div[2]/div/div[1]/div/div[2]/div/div[2]')))
anzoategui.click() 

# clic boton ciudad
citybutton = WebDriverWait(driver, 60).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/fieldset[4]/div[2]/div/button')))
citybutton.click()

# clic elegir lecheria
lecheria =driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/main/div/div[1]/div[2]/div/div[1]/div/div[2]/fieldset[4]/div[2]/div/div[1]/div/div[2]/div/div[20]/input')
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)",lecheria)
lecheria.click()

time.sleep(5)

## Datos a guardar
tipo = driver.find_element(By.XPATH, '//div[@class="flex-grow-1 d-flex flex-column bd-highlight mb-3 position-relative"]/div[@class="text-truncate text-capitalize mb-0 small pb-1 text-info fw-bold "]').text
tipovivienda = driver.find_element(By.XPATH, '//div[@class="flex-grow-1 d-flex flex-column bd-highlight mb-3 position-relative"]/a[@class="text-decoration-none h5 link-dark text-truncate text-capitalize mb-0 stretched-link "]').text
precio = driver.find_element(By.XPATH, '//div[@class="flex-grow-1 d-flex flex-column bd-highlight mb-3 position-relative"]/div[@class="row  justsify-content-between mt-auto"]/div[@class="col-12"]/h5').text
ubicacion = driver.find_element(By.XPATH, '//div[@class="flex-grow-1 d-flex flex-column bd-highlight mb-3 position-relative"]/div[@class="text-muted font-weight-light text-truncate small m-0"]').text
terreno = driver.find_element(By.XPATH,'//div[@class="flex-grow-1 d-flex flex-column bd-highlight mb-3 position-relative"]/div[@class="mt-2 text-muteds text-truncate small"]/span[@class=""][1]/span[@class="fw-bolds"]').text
construccion = driver.find_element(By.XPATH,'//div[@class="flex-grow-1 d-flex flex-column bd-highlight mb-3 position-relative"]/div[@class="mt-2 text-muteds text-truncate small"]/span[@class=""][2]/span[@class="fw-bolds"]').text

habitaciones = driver.find_element(By.XPATH,'//div[@class="flex-grow-1 d-flex flex-column bd-highlight mb-3 position-relative"]/div[@class="mb-2 text-muteds text-truncate small"]/span[@class="me-3"][1]').text
banos = driver.find_element(By.XPATH, '//div[@class="flex-grow-1 d-flex flex-column bd-highlight mb-3 position-relative"]/div[@class="mb-2 text-muteds text-truncate small"]/span[@class="me-3"][2]').text
estacionamientos = driver.find_element(By.XPATH, '//div[@class="flex-grow-1 d-flex flex-column bd-highlight mb-3 position-relative"]/div[@class="mb-2 text-muteds text-truncate small"]/span[@class="me-3"][3]').text
link = driver.find_element(By.XPATH, '//div[@class="col text-end"]/a').get_attribute("href")
pool=driver.find_element(By.XPATH, '//div[@class="flex-grow-1 d-flex flex-column bd-highlight mb-3 position-relative"]/div[@class="mb-2 text-muteds text-truncate small"]/span[@class="me-3"][5]').text
if pool == 'Piscina':
    pool=True
else:
    pool=False
print(tipo, tipovivienda, precio, 
      ubicacion, terreno, construccion, 
      habitaciones, banos, estacionamientos, 
      link, pool)
