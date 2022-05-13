# Importando bibliotecas

import requests # permite fazer uso do HTTP dentro dos seus programas Python em um formato legível
from bs4 import BeautifulSoup # projetado para fazer web scraping rapidamente

# Página home 
    """
    """
page = requests.get('https://www2.uab.pt/guiainformativo/cursos2.php')


# Criando objeto BeautifulSoup
    """
    Esse objeto utiliza como argumento o documento page.text do Requests (o conteúdo da resposta do servidor) 
    e então o analisa através do html.parser interno do Python.
    """

soup = BeautifulSoup(page.text, 'html.parser')