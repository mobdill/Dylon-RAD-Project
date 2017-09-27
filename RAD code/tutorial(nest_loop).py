Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:07:06) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for i in range (0,5):
	for a in range (0,5):
		print(a)

		
0
1
2
3
4
0
1
2
3
4
0
1
2
3
4
0
1
2
3
4
0
1
2
3
4
>>> 5%2
1
>>> 6%3
0
>>> 5/2
2.5
>>> fo i in range (2,30):
	
SyntaxError: invalid syntax
>>> for i in range (2,30):
	 j = 2
	 counter = 0
	 while j < i:
		 if i % j == 0:
			 counter = 1
		else :
			
SyntaxError: unindent does not match any outer indentation level
>>> 
>>> for i in range(2,30):
	j=2
	counter=0
	while j<i:
		if i % j==0:
			counter=1
		else:
			j=j+1
	if counter==1:
		print(i+"is a prime number.")
		counter=0

		
