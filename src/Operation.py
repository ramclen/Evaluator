from src.Result import *


class Operation(Result):
  symbol = ''
  number1 = 0
  number2 = 0


  def __init__(self, symbol, number1, number2):
    self.symbol = symbol
    self.number1 = number1
    self.number2 = number2

  def getResult(self):
    return self.number1.getResult() + self.symbol + self.number2.getResult()

