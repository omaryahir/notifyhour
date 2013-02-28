# This software send every hour some notification in Mac OSX
# It requires: https://github.com/setem/pync

from os import system
from pync import Notifier
import datetime 

print "Working process ...   [Press Ctrl+C for exit]"
print "Powered by Python, Mac OSX & https://github.com/setem/pync"

enviemensaje = False
activaalarma = False
now = datetime.datetime.now()
while now.hour<=18:
    now = datetime.datetime.now()
    if now.minute == 0:
        if not enviemensaje:
        	system('say Omar, descansa un momento tus ojos, recuerda Dios te ama.')
            mensaje = "Dios te ama, descansa un momento "+str(now.hour)+":"+str(now.minute)        
            Notifier.notify(str(mensaje))
            enviemensaje=True
            activaalarma=True
    
    if now.minute == 1:
        enviemensaje=False        

    if now.minute == 3:
    	if activaalarma:    		
    		system('say Listo, ahora puedes continuar trabajando, debes tener fe, todo estará bien.')
    		activaalarma=False

Notifier.notify("Sea como sea Omar hiciste tu mejor esfuerzo, vamonos..!")