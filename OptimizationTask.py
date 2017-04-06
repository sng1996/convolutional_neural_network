import Cell

class OptimizationTask:
    # x - variables
    task = None
    strategy = None
    cells = Cell.Cell()

    def OptimizationTask(self):
        pass

    def objective (self, x):
        print "objective calculation X"

    def constrants (self,x):
        print "calculation constrains values"

    def criteria (self):
        print "calculation criterias"

    def init (self):
        print "optimizationTask init (create objective)"
        #self.cells = Cell.Cell()
        self.objective(0)
        self.constrants(0)
        self.criteria()


    def gradient (self,x, strategy):
        print "calculation OPTask gradient"
        return strategy.gradient(self.cells, x)