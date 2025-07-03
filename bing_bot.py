from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import openai
import os
from dotenv import load_dotenv

def validar_existencia (driver, timeout=10):
    try:
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CLASS_NAME, "bnp_btn_accept"))
        )
        return True
    except TimeoutException:
        return False


def aceitar_cookies (driver):
    validar = validar_existencia(driver, 5)

    if validar:
        try:
            aceito = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "bnp_btn_accept"))
            )
            driver.execute_script("arguments[0].click();", aceito)
            print('Cookie aceito!')
        except Exception as e:
            print(f"Erro ao aceitar Cookies da pagina: {e}")
    else:
        print('elemento não encontrado')


def retornar_lista_de_pesquisa ():
    load_dotenv()
    chave = os.getenv("GPT_KEY")
    
    prompt = 'Liste 30 ideias de pesquisa e curiosidades de tecnologia e futebol.'
    openai.api_key = chave
    
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7        
    )
    resposta = response.choices[0].message.content
    print(resposta)
    return resposta

options = webdriver.EdgeOptions()
options.add_argument(f"user-data-dir=C:/EdgeSeleniumProfile")
options.add_argument("profile-directory=Default")

driver = webdriver.Edge(options=options)

driver.get("https://www.bing.com")
aceitar_cookies(driver)
sleep(10)
try:
    pesquisas = retornar_lista_de_pesquisa()
except:
    pesquisas = ['Globo', 'Cruzeiro', 'Libertadores', 'Iphone', 'Xbox', 'Maior de Minas', 'Times brasileiros no EAFC', 'Selenium Python', 'Data Engeneering', 'Mac OS',
    'Call of Duty', 'Python Data skills', 'Linguagem de programação', 'Teofilo Otoni', 'Mineirão', 'Cursor', 'Develop with WebDriver', 'GPT', 'Bing AI', 'MVC Pattern']

if pesquisas is not None:
    for nome in pesquisas:
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(nome)
        search_box.submit()
        aceitar_cookies(driver)
        sleep(10)
else:
    print("Não há nada para pesquisar")

driver.quit()