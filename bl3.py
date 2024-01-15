fi = open("XEPHANG.TXT",'r')
fo = open("XEPHANG.OUT","w")
mydict = {}

n, k = map(float, fi.readline().split())
n=int(n)

# print(n,k)
a = list(map(float, fi.readline().split()))
print(len(a))
# print(a)
print(a.count(9.7))
print(len(a))
# print(a[0])
# print(a[len(a)-1])
mydict = {}
for i in range(n):
    mydict.setdefault(a[i], 0)
    mydict[a[i]] = mydict.get(a[i])+1
    # print(a[i], mydict.get(a[i]))
# print(mydict)