from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import logging
import feedparser

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

def get_palavras ():
    feed = feedparser.parse('https://g1.globo.com/rss/g1/')
    titulos = [entry.title for entry in feed.entries]
    return titulos[:30]

def main():
    try:
        options = webdriver.EdgeOptions()
        options.add_argument(f"user-data-dir=C:/EdgeSeleniumProfile")
        options.add_argument("profile-directory=Default")

        list_palavras = get_palavras()

        driver = webdriver.Edge(options=options)
        driver.get("https://www.bing.com")  
        
        # aceitar_cookies(driver)

        if not list_palavras:
            logging.warning('Buscando lista de palavras padrão!')
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
        else:
            logging.warning('Buscando headres de noticias!')
            pesquisas = list_palavras

        if pesquisas is not None:
            for nome in pesquisas:
                search_box = driver.find_element(By.NAME, "q")
                search_box.clear()
                search_box.send_keys(str(nome))
                search_box.submit()
                aceitar_cookies(driver)
                sleep(10)
        else:
            raise Exception('Erro ao percorrer lista de palavras.')  
    except Exception as e:
        logging.critical(f'Erro ao executar processo!\n {e}')
    finally:
        driver.quit()

if __name__ == '__main__':
    main()