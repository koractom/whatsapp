import webbrowser
import time
t = 30 # tiempo de ejecucion bucle while metodo sleept
def envio(num1):
    link = "https://web.whatsapp.com/send?phone=" + str(num1) + "&text=hola,%20qué%20tal?"
    webbrowser.open(link)
f = open("tel.txt", "r")
while(True):
    time.sleep(t)
    linea = f.readline()
    envio(linea )
    if not linea:
        break
f.close()

#numero=int(input('introduce numero de telefono'))
#webbrowser.open('https://api.whatsapp.com/send?phone= + $numero + &text=hola,%20qué%20tal?')



#https://api.whatsapp.com/send?phone=34123456789&text=hola,%20qué%20tal?thonny