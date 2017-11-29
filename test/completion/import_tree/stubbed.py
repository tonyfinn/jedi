x = ['a', 'b']
mismatched = 5

class Foo:
    """
    Some class definition that is shadowed by 
    a type stub file.
    """
    x = 'Boo'
    excluded = 'Banana'

    def __init__(self, k):
        self.x = k

    def bar(self):
        return self.x