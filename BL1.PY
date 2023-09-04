# import o


s = str(input())
# file = open("")
sum=0;
for x in s:
    if x >= '0' and x <= '9':
        sum+=int(x)
print(sum)