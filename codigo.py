import pyautogui
import time
import pandas

# 1. Entrar no sistema da empresa
# 2. Fazer login
# 3. Importar a base de dados
# 4. Cadastrar 1 produto
# 5. Repetir 4 até acabar os produtos

pyautogui.PAUSE = 1

# 1. Entrar no sistema da empresa
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

link = "https://drive.google.com/drive/folders/1l9iQXjwRqkR0d9w3Vr7VY6tVZuT6UW4K?usp=sharing" # Link do site
pyautogui.write(link)
pyautogui.press('enter')

time.sleep(3)

# 2. Fazer login
#pyautogui.click(x=400, y=300)
pyautogui.write('seu_email')
pyautogui.press('tab')
pyautogui.write('sua_senha')
pyautogui.press('enter')

# 3. Importar a base de dados
tabela_produtos = pandas.read_csv("produtos.csv")

print(tabela_produtos)

# 4. Cadastrar 1 produtos
for linha in tabela_produtos.index:
    # 4. Cadastrar 1 produtos
    pyautogui.click(x=400, y=300) # Clicar no primeiro campo
    # Preenche os campos do formulario
    pyautogui.write(tabela_produtos.loc[linha,"codigo"])
    pyautogui.press('tab')
    pyautogui.write(tabela_produtos.loc[linha,"marca"])
    pyautogui.press('tab')
    pyautogui.write(tabela_produtos.loc[linha,"tipo"])
    pyautogui.press('tab')
    pyautogui.write(str(tabela_produtos.loc[linha,"categoria"]))
    pyautogui.press('tab')
    pyautogui.write(str(tabela_produtos.loc[linha,"preço"]))
    pyautogui.press('tab')
    pyautogui.write(str(tabela_produtos.loc[linha,"custo"]))
    pyautogui.press('tab')
    if(tabela_produtos.loc[linha,"obs"] != ''):
        pyautogui.write(tabela_produtos.loc[linha,"obs"])
    pyautogui.press('tab')
    # Envia
    pyautogui.press('enter')
    # Retorna a tela para cima
    pyautogui.scroll(2000)