from src.Result import *


class Operation(Result):
  symbol = ''

  def __init__(self, symbol):
    self.symbol = symbol

  def getResult(self):
    raise NotImplementedError("Not implemented")

