class MarkedNode(Node):
    def __init__(self):
        super(self)
        self.marked_temporarily = False
        self.marked_permanently = False
