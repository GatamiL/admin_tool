from MainUI import Gui
from database import database
from webinterface import GetHandler
from threading import Thread
from http.server import HTTPServer
from webinterface import GetHandler



if __name__ in '__main__':
    Thread(target = Gui()).start()
    Thread(target = GetHandler.run()).start()