import threading




from leapupproject.WebSocket.WebSocketListener import WebSocketListener
from multiprocessing import Queue
import math


class Analysis(threading.Thread):
    def __init__(self,queue):
        super(Analysis, self).__init__()
        self.queue = queue
        self.calibrate = False
        self.exercise = False
        self.lenstart = []

    def run(self):
        while True:
            if not self.queue.empty():

                data = self.queue.get()
                if 'hands' in data and len(data["hands"]) > 0:
                    if 'pointables' in data and len(data["pointables"]) > 4:
                        #print(data)
                        thumb = (data['pointables'][0]['tipPosition'][0]-data["hands"][0]["palmPosition"][0],data['pointables'][0]['tipPosition'][1]-data["hands"][0]["palmPosition"][1],data['pointables'][0]['tipPosition'][2]-data["hands"][0]["palmPosition"][2])
                        pointer = (data['pointables'][1]['tipPosition'][0]-data["hands"][0]["palmPosition"][0],data['pointables'][1]['tipPosition'][1]-data["hands"][0]["palmPosition"][1],data['pointables'][1]['tipPosition'][2]-data["hands"][0]["palmPosition"][2])
                        middle = (data['pointables'][2]['tipPosition'][0]-data["hands"][0]["palmPosition"][0],data['pointables'][2]['tipPosition'][1]-data["hands"][0]["palmPosition"][1],data['pointables'][2]['tipPosition'][2]-data["hands"][0]["palmPosition"][2])
                        ring = (data['pointables'][3]['tipPosition'][0]-data["hands"][0]["palmPosition"][0],data['pointables'][3]['tipPosition'][1]-data["hands"][0]["palmPosition"][1],data['pointables'][3]['tipPosition'][2]-data["hands"][0]["palmPosition"][2])
                        little = (data['pointables'][4]['tipPosition'][0]-data["hands"][0]["palmPosition"][0],data['pointables'][4]['tipPosition'][1]-data["hands"][0]["palmPosition"][1],data['pointables'][4]['tipPosition'][2]-data["hands"][0]["palmPosition"][2])

                        pointerthumb = (data['pointables'][0]['tipPosition'][0]-data['pointables'][1]['tipPosition'][0],data['pointables'][0]['tipPosition'][1]-data['pointables'][1]['tipPosition'][1],data['pointables'][0]['tipPosition'][2]-data['pointables'][1]['tipPosition'][2])
                        middlepointer = (data['pointables'][1]['tipPosition'][0]-data['pointables'][2]['tipPosition'][0],data['pointables'][1]['tipPosition'][1]-data['pointables'][2]['tipPosition'][1],data['pointables'][1]['tipPosition'][2]-data['pointables'][2]['tipPosition'][2])
                        ringmiddle = (data['pointables'][2]['tipPosition'][0]-data['pointables'][3]['tipPosition'][0],data['pointables'][2]['tipPosition'][1]-data['pointables'][3]['tipPosition'][1],data['pointables'][2]['tipPosition'][2]-data['pointables'][3]['tipPosition'][2])
                        littlering = (data['pointables'][3]['tipPosition'][0]-data['pointables'][4]['tipPosition'][0],data['pointables'][3]['tipPosition'][1]-data['pointables'][4]['tipPosition'][1],data['pointables'][3]['tipPosition'][2]-data['pointables'][4]['tipPosition'][2])



                        tipYthumb = data['pointables'][0]['tipPosition'][1]
                        tipYpointer = data['pointables'][1]['tipPosition'][1]
                        tipYmiddle = data['pointables'][2]['tipPosition'][1]
                        tipYring = data['pointables'][3]['tipPosition'][1]
                        tipYlittle = data['pointables'][4]['tipPosition'][1]





                        lenpt = math.sqrt(math.pow(pointerthumb[0],2)+math.pow(pointerthumb[1],2)+math.pow(pointerthumb[2],2))
                        lenmp = math.sqrt(math.pow(middlepointer[0],2)+math.pow(middlepointer[1],2)+math.pow(middlepointer[2],2))
                        lenrm = math.sqrt(math.pow(ringmiddle[0],2)+math.pow(ringmiddle[1],2)+math.pow(ringmiddle[2],2))
                        lenlr = math.sqrt(math.pow(littlering[0],2)+math.pow(littlering[1],2)+math.pow(littlering[2],2))

                        lenpalmthumb = math.sqrt(math.pow(thumb[0], 2) + math.pow(thumb[1], 2) + math.pow(thumb[2], 2))
                        lenpalmpointer = math.sqrt(math.pow(pointer[0], 2) + math.pow(pointer[1], 2) + math.pow(pointer[2], 2))
                        lenpalmmiddle = math.sqrt(math.pow(middle[0], 2) + math.pow(middle[1], 2) + math.pow(middle[2], 2))
                        lenpalmring = math.sqrt(math.pow(ring[0], 2) + math.pow(ring[1], 2) + math.pow(ring[2], 2))
                        lenpalmlittle = math.sqrt(math.pow(little[0], 2) + math.pow(little[1], 2) + math.pow(little[2], 2))

                        costp = (thumb[0]*pointer[0] + thumb[1]*pointer[1] + thumb[2]*pointer[2])/((math.sqrt((math.pow(thumb[0],2))+(math.pow(thumb[1],2))+(math.pow(thumb[2],2))))
                                            *(math.sqrt(math.pow(pointer[0],2)+math.pow(pointer[1],2)+math.pow(pointer[2],2))))


                        cospm = (pointer[0]*middle[0] + pointer[1]*middle[1] + pointer[2]*middle[2])/((math.sqrt((math.pow(pointer[0],2))+(math.pow(pointer[1],2))+(math.pow(pointer[2],2))))
                                            *(math.sqrt(math.pow(middle[0],2)+math.pow(middle[1],2)+math.pow(middle[2],2))))

                        cosmr = (middle[0]*ring[0] + middle[1]*ring[1] + middle[2]*ring[2])/((math.sqrt((math.pow(middle[0],2))+(math.pow(middle[1],2))+(math.pow(middle[2],2))))
                                            *(math.sqrt(math.pow(ring[0],2)+math.pow(ring[1],2)+math.pow(ring[2],2))))

                        cosrl = (ring[0]*little[0] + ring[1]*little[1] + ring[2]*little[2])/((math.sqrt((math.pow(ring[0],2))+(math.pow(ring[1],2))+(math.pow(ring[2],2))))
                                            *(math.sqrt(math.pow(little[0],2)+math.pow(little[1],2)+math.pow(little[2],2))))

                        tpR = math.acos(costp)
                        pmR = math.acos(cospm)
                        mrR = math.acos(cosmr)
                        rlR = math.acos(cosrl)

                        kattp = math.degrees(tpR)
                        katpm = math.degrees(pmR)
                        katmr = math.degrees(mrR)
                        katrl = math.degrees(rlR)

                        # tp = (thumb[0]-pointer[0],thumb[1]-pointer[1],thumb[2]-pointer[2])
                        # pm = (pointer[0]-middle[0],pointer[1]-middle[1],pointer[2]-middle[2])
                        # mr = (middle[0]-ring[0],middle[1]-ring[1],middle[2]-ring[2])
                        # rl = (ring[0]-little[0],ring[1]-little[1],ring[2]-little[2])

                        # if(tp>0,45 and tp<0,55 and pm>0,2 and pm<0,3 and mr>0,2 and mr<0,3 and rl>0,65 and rl<0,75):
                        #      print("stan poczatkowy ")
                        # if(tp>0,6 and tp<0,8 and pm>0,4 and pm<0,6 and mr>0,3 and mr<0,5 and rl>0,4 and rl<0,6):
                        #     print("stan koncowy")

                        def savelen(calibrate, lenstart):
                            self.calibrate = calibrate
                            self.lenstart = lenstart

                            if(self.calibrate==False):
                                if(lenpt>60 and lenpt<70 and lenmp>20 and lenmp<30 and lenrm>20 and lenrm<30 and lenlr>27 and lenlr<32):
                                    #dodanie do listy
                                    self.lenstart.append(lenpt)
                                    self.lenstart.append(lenmp)
                                    self.lenstart.append(lenrm)
                                    self.lenstart.append(lenlr)
                                    print(lenstart)
                                    print(lenpt - lenstart[0])
                                    #kalibracja true
                                    print("KALIBRACJA DZIALA !!! ")
                                    self.calibrate= True


                        def comparelen(exercise,calibrate):
                            self.calibrate = calibrate
                            self.exercise = exercise
                            if(self.exercise == False and self.calibrate == True):
                                if(lenpt - self.lenstart[0]>27 and lenmp - self.lenstart[1]>14 and lenrm - self.lenstart[2]>12 and lenlr - self.lenstart[3]>10):
                                    print("CWICZENIE WYKONANE PRAWIDLOWO !!! ")
                                    # print("Pierwsza odleglosc: " + str(lenpt - self.lenstart[0]))
                                    # print("Druga odleglosc: " + str(lenmp - self.lenstart[1]))
                                    # print("Trzecia odleglosc: " + str(lenrm - self.lenstart[2]))
                                    # print("Czwarta odleglosc: " + str(lenlr - self.lenstart[3]))
                                    if(lenpt - self.lenstart[0] < 10 and lenmp - self.lenstart[1] < 12 and lenrm - self.lenstart[2] < 12 and lenlr - self.lenstart[3] < 12):
                                        print("CWICZENIE WYKONANE PRAWIDLOWO 22222!!! ")
                                        self.exercise = True

                        # print("kciuk wskazujacy " + str(kattp))
                        # print("wksazujacy srodkowy " +str(katpm))
                        # print("srodkowy serdeczny " + str(katmr))
                        # print("serdeczny maly " +str(katrl))

                        # print("kciuk wskazujacy " + str(lenpt))
                        # print("wksazujacy srodkowy " + str(lenmp))
                        # print("srodkowy serdeczny " + str(lenrm))
                        # print("serdeczny maly " + str(lenlr))

                        # print("kciuk wskazujacy " + str(tp))
                        # print("wksazujacy srodkowy " + str(pm))
                        # print("srodkowy serdeczny " + str(mr))
                        # print("serdeczny maly " + str(rl))

                        # print("kciuk " + str(lenpalmthumb))
                        # print("wksazujacy " + str(lenpalmpointer))
                        # print("srodkowy " + str(lenpalmmiddle))
                        # print("serdeczny " + str(lenpalmring))
                        # print("maly " + str(lenpalmlittle))

                        # print("kciuk " + str(tipYthumb))
                        # print("wksazujacy " + str(tipYpointer))
                        # print("srodkowy " + str(tipYmiddle))
                        # print("serdeczny " + str(tipYring))
                        # print("maly " + str(tipYlittle))

                        savelen(self.calibrate,self.lenstart)
                        comparelen(self.exercise, self.calibrate)

    def join(self, timeout=None):

        super(Analysis, self).join(timeout)