# -*- encoding:utf8 -*-
# This software send every hour some notification in Mac OSX
# It requires: https://github.com/setem/pync

from os import system
from pync import Notifier
import datetime 

"""
NotifyHour

Powered by Python, Mac OSX & https://github.com/setem/pync"
"""

mensaje = 'Buen día Omar, todo estará bien vamos a trabajar.'
Notifier.notify(mensaje)
system('say '+mensaje)

enviemensaje = False
activaalarma = False
comida = True
now = datetime.datetime.now()
while now.hour<18:
    now = datetime.datetime.now()
    if now.minute == 0:
        if not enviemensaje:        	
            mensaje = "Dios te ama, descansa un momento "+str(now.hour)+":"+str(now.minute)        
            Notifier.notify(str(mensaje))
            system('say Omar, descansa un momento tus ojos, recuerda Dios te ama.')
            enviemensaje=True
            activaalarma=True
    
    if now.minute == 1:
        enviemensaje=False        

    if now.minute == 3:
    	if activaalarma:    		
    		system('say Listo, ahora puedes continuar trabajando, debes tener fe, todo estará bien.')
    		activaalarma=False

    if now.hour == 14:
        if now.minute >=30:
            if comida:
                system('say Omar, por favor ya ve a comer recuerda el boleto.')
                comida=False


mensaje = "Sea como sea Omar hiciste tu mejor esfuerzo, es hora de guardar y ¡vamonos!"
Notifier.notify(mensaje)
system('say '+mensaje)
