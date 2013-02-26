# This software send every hour some notification in Mac OSX
# It requires: https://github.com/setem/pync

from pync import Notifier
import datetime 

print "Working process ...   [Press Ctrl+C for exit]"
print "Powered by Python, Mac OSX & https://github.com/setem/pync"

enviemensaje = False
now = datetime.datetime.now()
while now.hour<=18:
    now = datetime.datetime.now()
    if now.minute == 0:
        if not enviemensaje:
            mensaje = "Dios te ama, descansa un momento "+str(now.hour)+":"+str(now.minute)        
            Notifier.notify(str(mensaje))
            enviemensaje=True
    if now.minute == 1:
        enviemensaje=False

Notifier.notify("Sea como sea Omar hiciste tu mejor esfuerzo, vamonos..!")