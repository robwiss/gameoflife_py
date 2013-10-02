
class Cell(object):
    __slots__ = ['_is_alive']

    def __init__(self, is_alive=False):
        self._is_alive = is_alive
    
    def is_alive(self):
        return self._is_alive
    
    def live(self):
        self._is_alive = True

    def die(self):
        self._is_alive = False
