fi = open("LWORD.INP", "r")
fo = open("LWORD.OUT", "w")
s=fi.readline()
a=s.split()
t=0   
for i in a:
    lenth=len(i)
    if lenth>t:
        t=lenth
fo.write(str(t))
fi.close()
fo.close()