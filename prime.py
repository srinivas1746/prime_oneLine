
##we can use lambda function for this

## range taken from 2 i.e exception of 1

primelist = lambda n : [x for x in range(2, n) if not 0 in map(lambda z : x % z, range(2,x))]



print(primelist(100))