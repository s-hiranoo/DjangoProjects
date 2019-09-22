class Node(object):
    id = 0
    value = ''
    children = []

    def __init__(self, _id=0, _value=''):
        self.id = _id
        self.value = _value
        return

    def set_id(self, _id):
        self.id = _id
        return

    def set_value(self, _value):
        self.value = _value
        return

    def add_children(self, _children):
        self.children += _children
        return

    def get_id(self):
        return self.id

    def get_value(self):
        return self.value

    def get_children(self):
        return self.children



