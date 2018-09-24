h=int(raw_input())
factor=0
for i in range(1,h):
    if h%i==0:
        factor=i
if factor>1:
    print "yes"
else:
    print "no"
