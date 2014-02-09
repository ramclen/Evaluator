from src.Number import *
from src.Operation import *

class Evaluator:

  operation = 0
  operationSymbols = ['*',':', '+','-']

  def getOperation(self, operation):
    for i in self.operationSymbols:
      for j in range(0,len(operation)):
        if i == operation[j]:
          self.operation = Operation(i, Number(operation[j+1]), Number(operation[j-1]))


    return self.operation

if __name__ == "__main__":
  evaluator = Evaluator
  result = evaluator.getOperation(evaluator, '1*3')
  print(result.getResult())