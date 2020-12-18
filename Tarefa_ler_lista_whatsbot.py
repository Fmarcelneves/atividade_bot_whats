# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:22:42 2020

@author: fmarc
"""

from time import sleep 
from whatsapp_api import WhatsApp 
import pandas as pd

#Inicializar o whatsapp
wp = WhatsApp()

#Esperar que enter seja pressionado
input("Pressione enter apos escanear o QR Code")

# Função para ler arquivos do excel
Contato = ['Lucas', 'Glaceir', 'Mauricio', 'Felipe']
Nome = ['Lucas', 'Glaceir', 'Mauricio', 'Felipe']
Mensagem = ['Olá, o bot do zap agradece sua existência'] * 4 

df = pd.DataFrame(data=zip(Contato, Nome, Mensagem), columns=['Contato','Nome','Mensagem'])
df.head()

nomes_palavras_chaves = list(df['Contato'])
nomes_palavras_chaves

lista_mensagens = list(df['Mensagem'])
lista_mensagens

for nome_pesquisar, mensagem in zip(nomes_palavras_chaves, lista_mensagens):
    # Pesquisar pelo contato e esperar um pouco
    wp.search_contact(nome_pesquisar)
    sleep(2)
    
    # Mensagem a ser enviada
    mensagem = lista_mensagens
    print(mensagem)
    
    # Enviar mensagem
    wp.send_message(mensagem)

# Esperar 10 segundos e fechar
sleep(10)
wp.driver.close()