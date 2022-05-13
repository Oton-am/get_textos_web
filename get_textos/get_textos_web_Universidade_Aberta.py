# Importando bibliotecas
import requests # permite fazer uso do HTTP dentro dos seus programas Python em um formato legível
from bs4 import BeautifulSoup # projetado para fazer web scraping rapidamente
import csv

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

arq_csv = csv.writer(open('cursos_e_planos_estudos_universidade_aberta.csv', 'w'))
arq_csv.writerow(['Curso', 'Plano de Estudos'])

# Selecionando a div que vamos coletar os dados
classe_cursos_name = soup.find(class_='subtitulo')

# Pegar o texto de todas as instâncias da tag <a> dentro da div BodyText
get_name_cursos = classe_cursos_name.find_all_next('a')



# loop para iterar sobre todas as tags <a> da classe 'area_texto
for curso in get_name_cursos:
    name_curso = curso.contents[0]
    link_plano_estudo = 'https://www2.uab.pt/guiainformativo/' + curso.get('href')
    
    # Adiciona nas linhas do arquivo CSV o nome do curso e o link para o plano de estudo
    arq_csv.writerow([name_curso, link_plano_estudo])