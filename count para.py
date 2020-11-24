filename = input("enter file name: ")
inf = open(filename, 'r')

linecount = 0
for i in inf:
   paragraphcount = 0
   if '\n' in i:
      linecount += 1
   if len(i) < 2: paragraphcount *= 0
   elif len(i) > 2: paragraphcount = paragraphcount + 1
   print('%-4d %4d %s' % (paragraphcount, linecount, i))  
inf.close()