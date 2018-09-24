k=int(raw_input())
if k>0:
    for i in range(2,k):
        if(k%i)==0:
            print "no"
            break
    else:
        print "yes"
