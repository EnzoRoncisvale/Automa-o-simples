import pyautogui
import time
import subprocess

pyautogui.pause = 0.5

# Abre o link em uma guia anônima
subprocess.Popen(['C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', '--incognito', 'https://castgroup.izeus.com.br/ponto'])

pyautogui.moveTo(x=551, y=459)
pyautogui.sleep(2)
pyautogui.click(x=587, y=456)

pyautogui.write('LOGIN')

pyautogui.moveTo(x=549, y=525)
pyautogui.sleep(2)
pyautogui.click(x=549, y=525)

pyautogui.write('SENHA')

pyautogui.click(x=543, y=592)

pyautogui.sleep(5)

pyautogui.click(x=64, y=192)

pyautogui.sleep(3)

#CLICA NO MAIS
pyautogui.click(x=46, y=823)
pyautogui.sleep(1.5)


#move para selecionar a tab
pyautogui.moveTo(x=432, y=585)
pyautogui.click(x=432, y=585)
pyautogui.sleep(2)

pyautogui.moveTo(x=415, y=430)
pyautogui.click(x=415, y=430)
pyautogui.sleep(1)

#PRIMEIRA MARCACAO HORA
pyautogui.moveTo(x=671, y=816)
pyautogui.sleep(1)
pyautogui.click(x=671, y=816)
pyautogui.write ('14:01')
pyautogui.sleep(1)

#OUTRO MAIS
pyautogui.click(x=1020, y=810)
pyautogui.sleep(1)

pyautogui.click(x=721, y=809)
pyautogui.sleep(1)
pyautogui.write('18:06')

#dar o scroll para baixo

pyautogui.scroll(-180)
pyautogui.moveTo(x=1063, y=837)








