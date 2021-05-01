from selenium import webdriver
from time import sleep


navegador = webdriver.Chrome()  # cria um comando para abrir o navegador

# 1-> Entrar em https://ri.magazineluiza.com.br/default.aspx
navegador.get("https://ri.magazineluiza.com.br/default.aspx")  # navega até uma página específica

for i in range(2):
    navegador.find_element_by_xpath('//*[@id="owl-destaques"]/div[2]/div[1]/div[2]').click()
sleep(1)
# localiza um elemento pelo path dele
# 2-> Cicar em planilha dinâmica
navegador.find_element_by_xpath('//*[@id="owl-destaques"]/div[1]/div/div[4]/div/a/p').click()

# 3-> Clicar em "clique aqui para fazer o download"
navegador.find_element_by_xpath('//*[@id="4zS989en0CKjhpbeCLPGMw=="]').click()

