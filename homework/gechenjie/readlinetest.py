fo = open("D:/1.txt", "r")
print "Name of the file: ", fo.name
line = fo.readlines(10)
print "Read Line: %s" % (line)
print len(line)
line = fo.readline(8)
print "Read Line: %s" % (line)
print len(line)
# Close opend file
fo.close()
