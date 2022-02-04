import again
import listcomp
import file
import diff



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
if isinstance(person,Desc):
  print('Person is an instance of Desc')
s=0
i=0
while i<10:
  s+=i
 
print(person.printChar())
