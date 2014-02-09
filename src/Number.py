from src.Result import Result


class Number(Result):
  number = 0

  def __init__(self, number):
    self.number = number

  def getResult(self):
    return self.number