
def printName(name):
  print('your name is '+name+', vey pleased to meet you')
class Desc:
  names='Member of Desc'

  def __init__(self,name,age,yob):
    self.name=name
    self.age=age
    self.yob=yob
  
  def printChar(self):
    print('%s was born in %d and is %d years old'%(self.name,self.yob,self.age))
person=Desc('Steve',23,1994)

print(person.printChar())
