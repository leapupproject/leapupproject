import pygame
from leapupproject.WebSocket.WebSocketListener import WebSocketListener
from multiprocessing import Queue
from leapupproject.WebSocket.Window import Window
from leapupproject.project.analysis import Analysis


class MainApplication:

    def __init__(self):
        self.queue = Queue(maxsize=1)


        self.listener = WebSocketListener(self.queue)
        self.listener.daemon = True

        # self.window = Window(self.queue)
        # self.window.daemon = True
        self.a = Analysis(self.queue)
        self.a.daemon = True

    def mainloop(self):
        self.listener.start()
        self.a.start()
        print(self.queue.empty())
        # self.window.start()

        # self.window.join()
        self.a.join()
        self.listener.join()


if __name__ == "__main__":
    application = MainApplication()
    application.mainloop()
