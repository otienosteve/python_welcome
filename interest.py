def comp(array1, array2):
    
    if array1==None or array2==None:
        return False
    
    array1.sort()
    array2.sort()
    
    ls=[ i*i for i in array1 ]
    
    if ls==array2:
        return True
    else:
        return False
# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.