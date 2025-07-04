from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

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

options = webdriver.EdgeOptions()
options.add_argument(f"user-data-dir=C:/EdgeSeleniumProfile")
options.add_argument("profile-directory=Default")

driver = webdriver.Edge(options=options)

driver.get("https://www.bing.com")
aceitar_cookies(driver)
sleep(5)

pesquisas = [
  "Plataformização",
  "Engajamento",
  "Identidade esportiva",
  "Análise tática",
  "Scouting digital",
  "Performance atlética",
  "Preparação neurofísica",
  "Torcida inteligente",
  "Geolocalização de fãs",
  "Estatísticas preditivas",
  "Gamificação",
  "Gestão esportiva",
  "Ativação de marca",
  "Matchday experience",
  "Criptoativos esportivos",
  "Inteligência artificial",
  "Aprendizado de máquina",
  "Visão computacional",
  "Modelagem preditiva",
  "Sistemas autônomos",
  "Processamento de linguagem natural",
  "Internet das Coisas (IoT)",
  "Análise comportamental",
  "Engenharia de dados",
  "Interoperabilidade digital",
  "Infraestrutura em nuvem",
  "Blockchain",
  "Tokenização",
  "Realidade aumentada",
  "Cibersegurança"
]

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