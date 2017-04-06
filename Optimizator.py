import scipy
from scipy.optimize import minimize
import OptimizationTask
class Optimizator:

    x = []
    optimization_task = OptimizationTask.OptimizationTask()

    def optimize (self, gradient, objective):
        print "start optimizator work"

        res = minimize(objective, gradient)
        #strat.gradient(self.x),
        #print res[0], res[1]
        print "res[0] res[1]"
        return res
#                self.optimization_task.objective(self.x),
#                self.optimization_task.constrants(self.x),
#                self.optimization_task.cells.density)