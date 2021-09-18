# wapf (write a python functn) as input two parand
# display their addition as result

def add(n1, n2):
	res = n1 + n2
	print("res = ", res)

m1 = float(input(" enter first number "))
m2 = float(input(" enter second number "))
add(m1, m2)

# n1, n2 ==> functional parameter
# m1, m2 ===> actual prarameter
# fp and ap can have same name