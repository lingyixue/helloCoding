a=input('high:')
b=input('weight:')
h=float(a)
w=float(b)
BIM=w/pow(h,2)
if BIM<=18.5:
	print('underweight')
elif BIM<=25:
	print('normal')
elif BIM<=28:	
	print('overweight')
elif BIM<=32:	
	print('obesity')
else:
	print('severe obesity')

