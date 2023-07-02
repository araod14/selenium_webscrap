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
casas = driver.find_elements(By.XPATH, '//div[@class="col scrollbar"]/div[@class="row mt-4"]/div[@class="col-md-6"]')
for i in casas:
    #tipoventas = driver.find_elements(By.XPATH, '//div[@class="flex-grow-1 d-flex flex-column bd-highlight mb-3 position-relative"]/div[@class="text-truncate text-capitalize mb-0 small pb-1 text-info fw-bold "]')
    #tipo = [tipoventa.text for tipoventa in tipoventas]

    #tipoviviendas = driver.find_elements(By.XPATH, '//div[@class="flex-grow-1 d-flex flex-column bd-highlight mb-3 position-relative"]/a[@class="text-decoration-none h5 link-dark text-truncate text-capitalize mb-0 stretched-link "]')
    #viviendas = [tipovivienda.text for tipovivienda in tipoviviendas]

    #precios = driver.find_elements(By.XPATH, '//div[@class="flex-grow-1 d-flex flex-column bd-highlight mb-3 position-relative"]/div[@class="row  justsify-content-between mt-auto"]/div[@class="col-12"]/h5')
    #precio = [precio.text for precio in precios]

    #ubicaciones = driver.find_elements(By.XPATH, '//div[@class="flex-grow-1 d-flex flex-column bd-highlight mb-3 position-relative"]/div[@class="text-muted font-weight-light text-truncate small m-0"]')
    #direccion = [ubicacion.text for ubicacion in ubicaciones]

    #terrenos = driver.find_elements(By.XPATH,'//div[@class="flex-grow-1 d-flex flex-column bd-highlight mb-3 position-relative"]/div[@class="mt-2 text-muteds text-truncate small"]/span[@class=""][1]/span[@class="fw-bolds"]')
    #terreno = [terreno.text for terreno in terrenos]

    #construcciones = driver.find_elements(By.XPATH,'//div[@class="flex-grow-1 d-flex flex-column bd-highlight mb-3 position-relative"]/div[@class="mt-2 text-muteds text-truncate small"]/span[@class=""][2]/span[@class="fw-bolds"]')
    #construccion = [construccion.text if construccion else '' for construccion in construcciones]

    #habitaciones = driver.find_elements(By.XPATH,'//div[@class="flex-grow-1 d-flex flex-column bd-highlight mb-3 position-relative"]/div[@class="mb-2 text-muteds text-truncate small"]/span[@class="me-3"][1]')
    #hab = [habitacion.text for habitacion in habitaciones]

    banos = driver.find_elements(By.XPATH, '//div[@class="d-flex flex-wrap flex-xxl-nowrap justify-content-center"]')
    ban = [bano.text for bano in banos]
    """
    ban = []
    for i in banos:
        if i.text=='':
            ban.append('no')
        elif i.text:
            ban.append(i.text)
        else:
            ban.append('no')
    """

    #estacionamientos = driver.find_elements(By.XPATH, '//div[@class="flex-grow-1 d-flex flex-column bd-highlight mb-3 position-relative"]/div[@class="mb-2 text-muteds text-truncate small"]/span[@class="me-3"][3]')
    #estacion = [estacionamiento.text if estacionamiento.text else None for estacionamiento in estacionamientos]

    #pools = driver.find_elements(By.XPATH, '//div[@class="flex-grow-1 d-flex flex-column bd-highlight mb-3 position-relative"]/div[@class="mb-2 text-muteds text-truncate small"]/span[@class="me-3"][5]')
    #piscina = [True if pool.text == 'Piscina' else False if pool.text != None else False for pool in pools]

    #links = driver.find_elements(By.XPATH, '//div[@class="col text-end"]/a')
    #link = [link.get_attribute("href") for link in links]

    
#df = pd.DataFrame({
 #   "tipo":tipo, "viviendas":viviendas, "precio":precio,
 #   "direccion":direccion, "terreno":terreno})
 #   #"construccion":construccion,
    #"habitaciones":hab, "banos":bano, "estacionamientos":estacion,
    #"link":link

#df.to_csv('viviendas_lecheria.csv', index=False)
print(ban)
