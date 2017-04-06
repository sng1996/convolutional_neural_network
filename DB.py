import json

class DB:
    cellsTestArray = []

    listObjects = []

#   def BaseTestExamples(self, *params):
#        pass

#    def appTestExample(self, *Cells, *params):
#        pass

    def database(self):
        print "DB accesed"

    def create (path):
        pass

    def save (path, result):
        print "write into file " +  result

    def read(self, path):
        f = open(path, 'r')
        result = f.read()
        print "read from file " +  result
        parsed_string = json.loads(result)

    def getAll(self):
        return self.listObjects

