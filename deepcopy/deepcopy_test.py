import copy

a = range(10)
b = a
c = copy.deepcopy(a)
a[0] = 1000

print "a is", a;
print "b is", b;
print "c is", c;
