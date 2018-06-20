

class hand():

    def __init__(self, hand):
        self.hand = hand

    def getData(self,data):
        self.data = data

    def dataToFinger(self):
            self.hand[0] = {"thumb":(self.data['pointables'][0]['tipPosition'][0],self.data['pointables'][0]['tipPosition'][1],self.data['pointables'][0]['tipPosition'][2])}
            self.hand[1] = {"pointer":(self.data['pointables'][1]['tipPosition'][0],self.data['pointables'][1]['tipPosition'][1],self.data['pointables'][1]['tipPosition'][2])}
            self.hand[2] = {"middle":(self.data['pointables'][2]['tipPosition'][0],self.data['pointables'][2]['tipPosition'][1],self.data['pointables'][2]['tipPosition'][2])}
            self.hand[3] = {"ring":(self.data['pointables'][3]['tipPosition'][0],self.data['pointables'][3]['tipPosition'][1],self.data['pointables'][3]['tipPosition'][2])}
            self.hand[4] = {"little":(self.data['pointables'][4]['tipPosition'][0],self.data['pointables'][4]['tipPosition'][1],self.data['pointables'][4]['tipPosition'][2])}
            self.hand[5] = {"palm":(self.data["hands"][0]["palmPosition"][0],self.data["hands"][0]["palmPosition"][1],self.data["hands"][0]["palmPosition"][2])}
