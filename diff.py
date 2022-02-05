#get values that are not duplicate in a list
def getDiff():
  ls=[1,2,3,4,5,6,7,9,1,2,3,5,6,7,8]
  l3=[11,12,13,14]
  l3.extend(l3)
  diff=set(l3)-set(ls)
  df=list(diff)
  print(df)
print('What are you up to??')
