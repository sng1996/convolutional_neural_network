import Cell
import DB
import OptimizationTask
import Solver
import StrategySearch
import Strategy
import Optimizator

class Task:

    #concrete task

    input_file = ""
    task_type = "" # task type
    solver= ""
    result_file = ""
    cells = []


   def solve (x):
       solver.setDensity(x)#pyfoam
       code = solver.solve()
       cells = solver.read_results()

       return (code, cells)

   def donext(self):
         pass

   def learnOnSet(set_name):
       sets = db.readSet(set_name)
       strategy = Strategy.Strategy()
       for i in sets:
           var = i
           self.learnVariant(strategy)
       db.save(strategy, "result.txt")

   def learnVariant(self, strategy):
        db = DB.DB()
        task = db.readTask("hello.txt")
        cells = Cell.Cell()
        optTask = task.optTask() #OptimizationTask.OptimizationTask()
        #optTask.init()
        #solver = task.solver() # Solver.Solver()
        #solver.run(optTask.task)
        #solver.check()
        #Vanya_krasavchik


        #strategy = Strategy.Strategy()
        optimizator = Optimizator.Optimizator()
        strategySearch = StrategySearch.StrategySearch()
        strategy = strategySearch.search(strategy, optimizator, task)
        #optTask.gradient(0, strategy)

        self.donext()

        #db.save(strategy, "result.txt");

        return strategy

task = Task()
task.run()