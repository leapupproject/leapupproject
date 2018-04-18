from leapupproject.WebSocket.WebSocketListener import WebSocketListener
from queue import Queue


class MainApplication:

    def __init__(self):
        self.queue = Queue()
        self.listener = WebSocketListener(self.queue)
        self.listener.daemon = True

    def mainloop(self):
        self.listener.start()

        while True:
            result = self.queue.get()

        self.listener.join()


if __name__ == "__main__":
    application = MainApplication()
    application.mainloop()
