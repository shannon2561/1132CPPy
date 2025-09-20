# a=7.5
# b=7.5
# c=7.5

a=float(input())
b=float(input())
c=float(input())

#1
perimeter=a+b+c
print(f"Perimeter: {perimeter:.1f}")

#2
s=perimeter/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(f"Area: {area:.1f}")

#3
if a==b==c:
    print("Type: Equilateral Triangle")
elif a==b or a==c or b==c:
    print("Type: Isosceles Triangle")
else:
    print("Type: Scalene Triangle")

#elif a!=b and b!=c and a!=c:
#    print("Type: Scalene Triangle")
#else:
#    print("Type: Isosceles Triangle")