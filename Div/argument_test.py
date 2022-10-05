import sys
 
#if len(sys.argv) < 1:
    #print("no arg given")
    #exit()
#n = int(sys.argv[1])
#print(n+1)

if len(sys.argv) > 1:
    blah = sys.argv[1]
else:
    blah = 'blah'

print(blah)