from collections import defaultdict
import json

class MarkingPositionMonitor:
    def __init__(self):
        self.pos = defaultdict(lambda: 0)
        self.orders = {}

    def on_event(self, message):
        msg = json.loads(message)
        if msg["type"] == "NEW":
            self.on_new_order(msg)
        elif msg["type"] == "ORDER_REJECT":
            self.on_order_reject(msg)
        elif msg["type"] == "CANCEL_ACK":
            self.on_cancel_ack(msg)
        elif msg["type"] == "FILL":
            self.on_fill(msg)
        return self.pos[self.orders[msg["order_id"]].symbol]

    def on_fill(self, msg):
        order = self.orders[msg["order_id"]]
        if order.side == "BUY":
            self.pos[order.symbol] += msg["filled_quantity"]
            order.quantity = msg["remaining_quantity"]

    def on_cancel_ack(self, msg):
        order = self.orders[msg["order_id"]]
        if order.side == "SELL":
            self.pos[order.symbol] += order.quantity

    def on_new_order(self, msg):
        order = Order(msg["order_id"], msg["type"], msg["side"], msg["symbol"], msg["quantity"])
        self.orders[msg["order_id"]] = order
        if order.side == "SELL":
            self.pos[order.symbol] -= order.quantity

    def on_order_reject(self, msg):
        order = self.orders[msg["order_id"]]
        if order.side == "SELL":
            self.pos[order.symbol] += order.quantity


class Order:
    def __init__(self, id, type="", side="", symbol="", quantity=0):
        self.id = id
        self.type = type
        self.side = side
        self.symbol = symbol
        self.quantity = quantity

    def __repr__(self):
        return "{} {} {} {}".format(self.type, self.side, self.symbol, self.quantity)


messages = [
    '{"type": "NEW", "symbol": "IMIMP", "order_id": 1, "side": "SELL", "quantity": 800, "time": "2017-03-15T10:15:10.975187"}'
]

m = MarkingPositionMonitor()
print(m.on_event(messages[0]))
