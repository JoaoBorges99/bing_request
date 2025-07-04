# Bing Bot - Automatizando Pesquisas com Selenium

Este projeto é um bot automatizado em Python que realiza buscas no Bing utilizando o Selenium WebDriver. Ele pode buscar termos vindos de um feed RSS de notícias ou de uma lista pré-definida. O bot também aceita cookies automaticamente ao acessar o site.

## Pré-requisitos

- Python 3.8+
- [Selenium](https://pypi.org/project/selenium/)
- [feedparser](https://pypi.org/project/feedparser/)
- Microsoft Edge instalado
- [Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) compatível com a versão do seu navegador

## Instalação

1. Clone este repositório:
   ```sh
   git clone https://github.com/JoaoBorges99/bing_request.git
   cd seu-repo
   ```

2. Instale as dependências:
   ```sh
   pip install selenium feedparser
   ```

3. Baixe o Edge WebDriver e coloque o executável no PATH do sistema ou na mesma pasta do script.

## Estrutura do Código

- `validar_existencia(driver, timeout)`: Aguarda até que o botão de aceitar cookies esteja presente na página.
- `aceitar_cookies(driver)`: Aceita os cookies se o botão estiver disponível.
- `get_palavras()`: Busca os 30 primeiros títulos do feed RSS do G1.
- O script configura o perfil do navegador, abre o Bing, aceita cookies e realiza buscas para cada termo.

## Passo a Passo da Criação do Bot

1. **Importação de Bibliotecas**
   - Importa Selenium, feedparser e outras utilidades necessárias.

2. **Definição das Funções**
   - Cria funções para validar a existência do botão de cookies, aceitar cookies e buscar palavras do feed RSS.

3. **Configuração do Navegador**
   - Define opções do Edge, incluindo o uso de um perfil de usuário para manter sessões e cookies.

4. **Coleta de Palavras-Chave**
   - Tenta obter títulos do feed RSS. Se falhar, utiliza uma lista fixa de palavras.

5. **Execução das Pesquisas**
   - Para cada termo, localiza a barra de pesquisa do Bing, insere o termo, envia a busca e aceita cookies novamente se necessário.

6. **Finalização**
   - Fecha o navegador ao final do processo.

## Como Executar

1. Certifique-se de que o Edge WebDriver está disponível.
2. Execute o script:
   ```sh
   python bing_bot.py
   ```
3. O bot abrirá o Edge, aceitará cookies e fará buscas automaticamente.

## Observações

- O bot utiliza um perfil de usuário para evitar pop-ups recorrentes e manter sessões.
- O tempo de espera (`sleep`) pode ser ajustado conforme a velocidade da sua conexão.
- O feed RSS pode ser alterado para qualquer outro de sua preferência.

---

Sinta-se à vontade para adaptar