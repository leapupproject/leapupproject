import _thread as thread
import time
import json
import websocket
data = []


def on_message(ws, message):
    data.append(message)
    print(data)
    json.dumps(data)
    with open('data.json', 'w') as outfile:
        json.dump({"data" : data}, outfile)
    #print('Message: {0}'.format(message))


def on_error(ws, error):
    print(error)


def on_close(ws):

    print("### closed ###")


def on_open(ws):
    ws.send(json.dumps({"background": True}))

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:6437/",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()

