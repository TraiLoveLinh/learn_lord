import math
a = float(input("nhap so a: "))
b = float(input("nhap so b: "))
c = float(input("nhap so c: "))
den_ta = b ** 2 - 4 * a * c
print(den_ta)
if den_ta > 0:
    print("phuong trinh co 2 nghiem phan biet: x1 =", (- b + math.sqrt(den_ta)) /(2 * a),"x2 =", (- b - math. sqrt(den_ta)) /(2 * a))
elif den_ta == 0:
    print("phuong trinh co nghiem kep: x1 = x2 =", -b / 2 * a)
else:
    print("phuong trinh vo nghiem nhaaa")