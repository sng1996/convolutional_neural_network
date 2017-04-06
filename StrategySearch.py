import DB

class StrategySearch:

    numCells = 1000

    def learn (self, x): #res, strategy, tasks):
        print "learning from tasks"

        task.solve(x)
        obj = task.objective(x)
        cells = task.Cells()

        do_learn(strategy, obj, cells)

        return obj

    def search (self, strategy, optimizator, task):
        print "begin search"
        #db = DB.DB()

        #print "take from DB"

        #tasks = db.getAll()

        #print "learning from optimizator"

        i = 0

        #while(i < self.numCells):

        initCells()
        res = optimizator.optimize(strategy.gradient, self.learn)
#            self.learn (res, strategy, tasks)
#            i = i +  1
        return strategy

    def initCells(self):
        for i in cells:
            i.init()
            i.vars["density"] = 0.5
