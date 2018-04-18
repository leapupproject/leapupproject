import pygame
from leapupproject.WebSocket.WebSocketListener import WebSocketListener
from multiprocessing import Queue
import threading
import matplotlib.pyplot as plt

class MainApplication:

    def __init__(self):
        self.queue = Queue(maxsize=1)
        self.listener = WebSocketListener(self.queue)
        self.listener.daemon = True
        self.running = True
        self.p = threading.Thread(target=self.window, args=(self.queue,))
        self.p.start()

    def getData(self):
        self.queue.get()
        data = self.queue.get()
        if 'hands' in data and len(data["hands"]) > 0:
            x = data["hands"][0]["palmPosition"][0]
            y = data["hands"][0]["palmPosition"][1]
            z = data["hands"][0]["palmPosition"][2]
            return (x, y, z)
        return (0, 0, 0)

    # def plot(self):
    #     x,y,z = self.getData()
    #     print(x)
    #     plt.scatter(x, y, label="lab")
    #     plt.legend()
    #     plt.show()
    #     plt.draw()
    def window(self, queue):
        q = queue
        BLUE = (0, 0, 255)
        RED = (255, 0, 0)
        background_colour = (0, 0, 0)
        (width, height) = (1200, 602)
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Tutorial 1')
        screen.fill(background_colour)

        pygame.display.flip()

        running = True
        while running:
            ev = pygame.event.get()

            data = q.get()
            print(data)
            if 'hands' in data and len(data["hands"]) > 0:
                x = data["hands"][0]["palmPosition"][0]
                y = data["hands"][0]["palmPosition"][1]
                z = data["hands"][0]["palmPosition"][2]
            else:
                x = 0
                y = 0
                z = 0
            if 'hands' in data and len(data["hands"]) > 1:
                x2 = data["hands"][1]["palmPosition"][0]
                y2 = data["hands"][1]["palmPosition"][1]
                z2 = data["hands"][1]["palmPosition"][2]
            else:
                x2 = 0
                y2 = 0
                z2 = 0
            pygame.draw.circle(screen, BLUE, (int(x) * 2 + 700, int(y) * 2), 12)
            pygame.draw.circle(screen, RED, (int(x2) * 2 + 700, int(y2) * 2), 12)
            pygame.display.update()
            for event in ev:

                if event.type == pygame.QUIT:
                    running = False

    done = True

    def mainloop(self):
        self.listener.start()

        self.p.join()
        self.listener.join()


if __name__ == "__main__":
    application = MainApplication()
    application.mainloop()
