
from tkinter.ttk import Label, Button, Combobox, Style
from tkinter import messagebox
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import threading
import pyautogui
pyautogui.useImageNotFoundException(False)

#CONFIGURAÇÕES INICIAIS PARA A INTERFACE------------------------------------------
root = ThemedTk(theme="black", themebg=True)
root.title("ChiloBot")
root.geometry("180x55+250+250")
root.resizable(False, False)
style = Style()
def generete_widget(widget, row, column, sticky="NSEW", columnspan=None, **kwargs):
    my_widget = widget(**kwargs)
    my_widget.grid(row=row, column=column, padx=5, pady=5, sticky=sticky)
    return my_widget
#-----------------------------------------------------------------------------------

#PUXANDO A IMAGEM PARA O PYTHON ----------------------------------------------------------------
def load_foto():
    load_image = Image.open('crystal_coin.png')
    return ImageTk.PhotoImage(load_image)
crystal_foto = load_foto()
label_gold_coin = generete_widget(Label, row=0, column=0, text='Converter Gold', font='impact')
#-----------------------------------------------------------------------------------------------


#START ---------------------------------------------------------------------------------------
def run():
    while True:
            check_gold()
            check_platinum()
#            threading.Thread(target=run)

run = threading.Thread(target=run).start

foto_crystal_coin = generete_widget(Button, row=0, column=1, image=crystal_foto, command=run)
# ---------------------------------------------------------------------------------------------

#CHECANDO GOLD COIN ----------------------------------------------
def check_gold():
    if pyautogui.locateOnScreen("gold_coin.png"):
        print('Achei o Gold Coin')
        pyautogui.center(pyautogui.locateOnScreen("gold_coin.png"))
        pyautogui.moveTo(pyautogui.locateOnScreen("gold_coin.png"))
        pyautogui.click(button='right')
#-----------------------------------------------------------------------

#CHECANDO PLATINUM COIN -----------------------------------------------
def check_platinum():
    if pyautogui.locateOnScreen("platinum_coin.png"):
        print('Achei o Platinum Coin')
        pyautogui.center(pyautogui.locateOnScreen("platinum_coin.png"))
        pyautogui.moveTo(pyautogui.locateOnScreen("platinum_coin.png"))
        pyautogui.click(button='right')  
#-----------------------------------------------------------------------


root.mainloop()


#para gerar o arquivo:  pyinstaller --onefile --noconsole --name=ChiloBot --icon=imagem main.py