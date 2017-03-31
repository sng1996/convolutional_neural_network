class OptimizationTask:

    task = null
    strategy = null

    def objective (self, x)
        pass

    def constrants (self,x)
        pass

    def criteria (self)
        pass

    def init (self)
        pass

    def gradient (self,x)

        return strategy.gradient(task.cells, x)