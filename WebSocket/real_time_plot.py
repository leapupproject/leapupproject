import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#import matplotlib import style

#style.use('ficethirtyeight')
class plotting():
    def __init__(self):
        
        self.fig = plt.figure()
        self.chart = self.fig.add_subplot(1,1,1)
        self.x=[]
        self.y=[]
        self.z=[]
        self.time=[]

        
    def animate(self, data):
        #if data is None:
         #   print('BLAD DANYCH!!!')

        #with open('data.json') as f:
            #data = json.load(f)
            
        #for number_of_second in range(1,len(data['data'])):
         #   self.time.append(number_of_second)

        for second in data['data']:
            try:
                if len(second['hands'])>0:
                    if(second['hands'][0]['palmPosition'][0]==self.x[-1]):
                        pass
                    else:
                        self.x.append(second['hands'][0]['palmPosition'][0])
                    if(second['hands'][0]['palmPosition'][1]==self.y[-1]):
                        pass
                    else:  
                        self.y.append(second['hands'][0]['palmPosition'][1])
                    if(second['hands'][0]['palmPosition'][2]==self.z[-1]):
                        pass
                    else:    
                        self.z.append(second['hands'][0]['palmPosition'][2])
            except (KeyError, IndexError):
                continue
        self.chart.clear()
        self.chart.plot(self.x)
        self.chart.plot(self.y)
        self.chart.plot(self.z)

    
        ani = animation.FuncAnimation(self.fig, self.animate, interval=1000)
        plt.show()
