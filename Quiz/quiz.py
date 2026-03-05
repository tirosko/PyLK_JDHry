def REVERSE(a): 
	a.reverse() 
	return(a) 
def YKNJS(a): 
	b = [] 
	b.extend(REVERSE(a)) 
	print(b) 

a = [1, 3.1, 5.31, 7.531] 
YKNJS(a)