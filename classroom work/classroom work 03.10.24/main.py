from __future__ import annotations

class Item:
    def __init__(self, value: int, nxt: item):
        self.value: int = value
        self.next: Item = nxt 

b = Item(2, None)
a = Item(1, b)

print(a.next.value)

class Linkedlost:
    def __init__(self, value: int, nxt: item):
        self.value: int = value
        self.next: Item = nxt 