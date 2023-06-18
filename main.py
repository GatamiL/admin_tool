from MainUI import Gui
from database import database
from webinterface import GetHandler

if __name__ in '__main__':
    Gui()

if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 31524), GetHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()