class Square(object):
    def __init__(self, length):
        self._length = length
    # Java-style
    def get_length(self):
        return self._length
    # Java-style
    def set_length(self, length):
        self._length = length

r = Square(5)
r.get_length()
r.set_length(6)
