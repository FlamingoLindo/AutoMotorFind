import requests
from bs4 import BeautifulSoup

# URL da página de onde você quer extrair dados
url = 'https://buscacep.com.br/estado/sao-paulo/sao-paulo'

# Realiza a requisição HTTP GET para a página
response = requests.get(url, timeout=10)  # Defina um timeout adequado

# Verifica se a requisição foi bem sucedida
if response.status_code == 200:
    # Usa BeautifulSoup para analisar o HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Encontra a tabela de CEPs na página
    table = soup.find('table', {'class': 'table-striped'})
    
    # Encontra todas as linhas da tabela
    rows = table.find_all('tr')
    
    # Pula a primeira linha que é o cabeçalho da tabela
    ceps = []
    for row in rows[1:]:  # Começa do segundo item para pular o cabeçalho
        cells = row.find_all('td')
        if cells:  # Verifica se há células na linha
            cep = cells[-1].text.strip()  # O CEP está na última célula
            ceps.append(cep)
    
    # Junta todos os CEPs em uma string, separados por vírgula
    cep_string = ','.join(ceps)
    print(cep_string)
else:
    print("Falha ao acessar a página:", response.status_code)
