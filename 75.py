i = raw_input().rstrip()
sLen = len(i)
mid = sLen >> 1
if (sLen & 1):
	print(i[:mid] + "*" + i[mid+1:])
else:
	print(i[:mid-1] + "**" + i[mid+1:])
