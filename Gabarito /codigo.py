import pyautogui # Biblioteca para automação de teclado, mouse, etc..
import time

# pyautogui.cliclk -> clicar em algum lugar 
# pyautogui.press -> apérta uma tecla  
# pyautogui.write -> escrever um texto 
# pyautogui.hotkey -> apertar uma combinaçlão de teclas  

pyautogui.PAUSE = 0.3

# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Abrir o Crhome
pyautogui.press("Win")
pyautogui.write("crhome")
pyautogui.press("enter")

# digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Espera 3 segundos 
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=649, y=464)
pyautogui.write("lucas__1994@hotmail.com")

# Preencher a senha
pyautogui.press("tab")
pyautogui.write("minhasenha")

# Botao Logar
pyautogui.press("tab")
pyautogui.press("enter")

# Espera 3 segundos 
time.sleep(3)


# Passo 3: Importar a base de dados 
import pandas 

tabela = pandas.read_csv("produtos.csv")


# Passo 4: Cadastrar um produto 
for linha in tabela.index: # para cada linha da minha tabela
    pyautogui.click(x=613, y=328)


    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab") # passar para o proximo campo
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab") # passar para o proximo campo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab") # passar para o proximo campo
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab") # passar para o proximo campo
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab") # passar para o proximo campo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab") # passar para o proximo campo
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab") # passo para o botao enviar 
    pyautogui.press("enter")

    pyautogui.scroll(10000)

# Passo 5: Repetir para todos os produtos


