# you need pydictionary

from PyDictionary import PyDictionary
import pyperclip



while 1 == 1:
    x = input(".exit to exit enter word: ")
    if x == '.exit':
        break

    try:
         
        pyperclip.copy(list(PyDictionary(x).getMeanings().get(x).values())[0][0])
        print(list(PyDictionary(x).getMeanings().get(x).values())[0][0]+"")

    except:
        print("idk what went wrong here is the raw data: "+ str(PyDictionary(x).getMeanings()))