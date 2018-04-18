import json
import websocket
from websocket import create_connection
import threading


class WebSocketListener(threading.Thread):

    def __init__(self, result_q):
        super(WebSocketListener, self).__init__()
        self.result_q = result_q
        self.stopRequest = threading.Event()
        websocket.enableTrace(True)
        self.ws = create_connection("ws://localhost:6437/")
        self.ws.send(json.dumps({"background": True}))

    def run(self):

        while not self.stopRequest.isSet():
            try:
                data = self.ws.recv()
                data = json.loads(data)
                self.result_q.put(data)
            except self.result_q.Empty:
                continue

    def join(self, timeout=None):
        self.stopRequest.set()
        super(WebSocketListener, self).join(timeout)
