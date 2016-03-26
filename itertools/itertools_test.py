import itertools

print "test from_iterable"
test = itertools.chain.from_iterable('qweasdzxc')
for arg in test:
    print arg

print "test combinations"
test2 = itertools.combinations([1, 2, 3, 4, 5], 2)
for arg in test2:
    print arg

print "test product"
test3 = itertools.product([1, 2, 3], [4, 5, 6], [7, 8, 9])
for arg in test3:
    print arg
