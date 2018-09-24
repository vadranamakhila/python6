b,n=map(int,raw_input().split())
g=b*n
for i in range(g+1):
	if (i*i)==g:
		print "yes"
		break
else:
	print "no"
