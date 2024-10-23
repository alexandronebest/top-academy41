import json
class Plane:
    def __init__(self,name: str, speed: float, weight: float):
        self.name: str = name
        self.speed: float = speed
        self.weight: float = weight

    def json(self) -> str:
        return json.dumps({
            
        })