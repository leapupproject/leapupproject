import pygame
from leapupproject.WebSocket.WebSocketListener import WebSocketListener
from multiprocessing import Queue
from leapupproject.WebSocket.Window import Window


class MainApplication:

    def __init__(self):
        self.queue = Queue(maxsize=1)

        self.listener = WebSocketListener(self.queue)
        self.listener.daemon = True

        self.window = Window(self.queue)
        self.window.daemon = True

    def mainloop(self):
        self.listener.start()
        self.window.start()

        self.window.join()
        self.listener.join()


if __name__ == "__main__":
    application = MainApplication()
    application.mainloop()
