#list comprehension in python
ls=['1','2','3','4','5','6','7','8','9','10']
def findSum(ls):
#sum all the numbers
  ls=[int(i) for i in ls]
  return sum(ls)