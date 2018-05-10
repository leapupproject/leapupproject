import pygame
import threading

from math import floor, log
import math

#from leapupproject.WebSocket import handClass

WHITE = (189, 195, 199)
YELLOW = (241, 196, 15)
RED = (231, 76, 60)
GREEN = (39, 174, 96)
LIGHTBLUE = (52, 73, 94)
DARKBLUE = (44, 62, 80)
BACKGROUND = (52, 73, 94)
ORANGE = (211, 84, 0)
BLACK = (0, 0, 0)


class Window(threading.Thread):
    def __init__(self, queue):
        super(Window, self).__init__()
        self.queue = queue
        self.stopRequest = threading.Event()
        self.running = True
        self.scale = 20
        self.sc = 1.0
        self.screen_x = 1600
        self.screen_y = 900
        self.name = "palm"
        #self.hand = handClass.hand()


    def clear(self):
        self.world.fill(DARKBLUE)
        self.display.fill(BLACK)
        self.time = 0

    def run(self):
        pygame.init()
        pygame.font.init()
        resolution = pygame.display.Info()
        self.myfont = pygame.font.SysFont("monospace", 16)
        self.myfont2 = pygame.font.SysFont("monospace", 12)

        # render text

        self.display = pygame.display.set_mode((self.screen_x, self.screen_y), pygame.FULLSCREEN)

        pygame.display.set_caption("Scrolling Camera")
        clock = pygame.time.Clock()
        self.world = pygame.Surface((10000, 10000))
        self.time = 0

        pygame.display.set_caption('Graph')
        self.world.fill(DARKBLUE)

        pygame.display.flip()
        while self.running:

            ev = pygame.event.get()

            self.drawfinger(self.name)


            pygame.display.update()
            for event in ev:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if (self.sc < 1.5):
                            self.sc += 0.5
                            self.clear()
                    if event.key == pygame.K_DOWN:
                        if (self.sc > 0.5):
                            self.sc -= 0.5
                            self.clear()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            self.name = "thumb"
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_2:
                            self.name = "pointer"
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_3:
                            self.name = "middle"
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_4:
                            self.name = "ring"
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_5:
                            self.name = "little"
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_6:
                            self.name = "palm"
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                if event.type == pygame.QUIT:
                    self.running = False

    def join(self, timeout=None):
        self.stopRequest.set()
        super(Window, self).join(timeout)

    def drawGraph(self, vector, label):

        pygame.draw.circle(self.world, GREEN, (int(self.time), int(vector[0] * self.sc) + 1 + 300), 2)
        pygame.draw.circle(self.world, RED, (int(self.time), int(vector[1] * self.sc) + 300), 2)
        pygame.draw.circle(self.world, YELLOW, (int(self.time), int(vector[2] * self.sc) + 1 + 300), 2)

        self.display.blit(self.world, (-self.time + 40, 0))
        pygame.draw.line(self.world, WHITE, (0, 300), (10000, 300), 2)
        self.time += 1
        text = self.myfont.render(label, 2, WHITE)
        scalaLabel = self.myfont.render("scala:" + str(self.sc), 2, WHITE)

        xLabel = self.myfont.render("x", 2, GREEN)
        yLabel = self.myfont.render("y", 2, RED)
        zLabel = self.myfont.render("z", 2, YELLOW)

        self.display.blit(self.world, (-self.time + 500, 0))

        self.display.blit(text, (self.screen_x*0.9, self.screen_y*0.1))

        self.display.blit(xLabel, (self.screen_x*0.9, self.screen_y*0.5))
        pygame.draw.rect(self.display, GREEN, pygame.Rect((self.screen_x*0.9 + 20, self.screen_y*0.5 + 5), (10, 10)))

        self.display.blit(yLabel, (self.screen_x*0.9, self.screen_y*0.52))
        pygame.draw.rect(self.display, RED, pygame.Rect((self.screen_x*0.9 + 20, self.screen_y*0.52 + 5), (10, 10)))

        self.display.blit(zLabel, (self.screen_x*0.9, self.screen_y*0.54))
        pygame.draw.rect(self.display, YELLOW, pygame.Rect((self.screen_x*0.9 + 20, self.screen_y*0.54 + 5), (10, 10)))

        self.display.blit(scalaLabel, (self.screen_x*0.9, self.screen_y*0.1+20))

        pygame.draw.rect(self.display, BLACK, pygame.Rect((0, 0), (50, 1200)))
        for x in range(0, self.screen_y, int(self.scale * self.sc)):
            pygame.draw.line(self.world, LIGHTBLUE, (0, x), (10000, x), 1)
            pointerLabel = self.myfont2.render(str(x - 300), 2, GREEN)
            if (x != 0):
                self.display.blit(pointerLabel, (20, x - 5))
        if (self.time == 10000):
            self.clear()

    def drawfinger(self, finger):
        self.finger = finger

        if self.finger == "thumb":
            self.drawer(0)
        elif self.finger == "pointer":
            self.drawer(1)
        elif self.finger == "middle":
            self.drawer(2)
        elif self.finger == "ring":
            self.drawer(3)
        elif self.finger == "little":
            self.drawer(4)
        elif self.finger == "palm":
            self.palmer()

    def drawer(self, index):
        data = self.queue.get()
        if 'pointables' in data and len(data["pointables"]) > 0:
            x = data['pointables'][index]['tipPosition'][0]
            y = data['pointables'][index]['tipPosition'][1]
            z = data['pointables'][index]['tipPosition'][2]
        else:
            x = 0
            y = 0
            z = 0


        self.drawGraph((x, y, z), self.finger)

    def palmer(self):
        data = self.queue.get()
        if 'hands' in data and len(data["hands"]) > 0:
            x = data["hands"][0]["palmPosition"][0]
            y = data["hands"][0]["palmPosition"][1]
            z = data["hands"][0]["palmPosition"][2]
        else:

            x = 0
            y = 0
            z = 0

        self.drawGraph((x, y, z), "palm")