#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 09:31:16 2024

@author: rosaelenamunoz
"""

import requests
from bs4 import BeautifulSoup

# URL de la página de Wikipedia que quieres scrapear
url = "https://es.wikipedia.org/wiki/Web_scraping"

# Hacer una solicitud GET a la página
response = requests.get(url)

# Analizar el contenido HTML de la página
soup = BeautifulSoup(response.text, 'html.parser')

# Extraer el título de la página
title = soup.find('h1', {'id': 'firstHeading'}).text

# Extraer el primer párrafo
first_paragraph = soup.find('p').text

print("Título:", title)
print("Primer párrafo:", first_paragraph)

