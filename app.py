"""
def preguntar_edad():
    edad=input("ingrese edad: ")
    return int(edad)
def segunda_anio(anios):
    return anios*365*24*3600

def calular_edades():
    edad=preguntar_edad()
    segundo=segunda_anio(edad)
    print(f"la edad es: {segundo}")

calular_edades()
"""




import requests
from bs4 import BeautifulSoup

requests=requests.get("https://www.garbarino.com/producto/smart-tv-hisense-32-hd-led-hle3217rt/5b119b7e68")
content=requests.content
soup=BeautifulSoup(content, "html.parser")
element=soup.find("span",{"id":"final-price","class":"value-item"})
#print(requests.content)

price_text=element.text.strip()
price_without_symbol=price_text[1:]

price=float(price_without_symbol)
if price<5000:
    print(f"{price} -> You should buy the tv")
else:
    print(f"{price} -> Do not buy, it's too expensive")

