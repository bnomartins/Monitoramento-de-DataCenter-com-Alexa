import requests
from bs4 import BeautifulSoup
page = ""

# print(page.status_code)
# print(page.content)
def verificar_temperatura():

    page = requests.get('http://ip/4sensor.htm')

    soup = ""
    soup = BeautifulSoup(page.content, 'html.parser')
    #alinhamento de tags para análise
    # print(soup.prettify())

    temp = soup.find_all('td')[1].get_text()
    hum = soup.find_all('td')[3].get_text()

    temperatura = temp.split('ºC')[0]
    humidade = hum.split('%')[0]
    page = ""
    monitor = [temperatura, humidade]
    return monitor


# print(monitor[1])

# print(monitor[1])
# import requests
# from bs4 import BeautifulSoup

# url = requests.get('http://10.239.83.210/4sensor.htm')

# soup = BeautifulSoup(url.content, 'html.parser')

# result = soup.find_all('td')[1].get_text()

# print(result)

