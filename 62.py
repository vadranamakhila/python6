s=raw_input()
"""if all(x in '01' for x in a):
    print "yes"
else:
    print "no"
    """
if not(s.translate(None,'01')):
    print "yes"
else:
    print "no"
