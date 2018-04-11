# fib.py

def fib(n):
	# fibonacci calculation that outputs a list
	fibseq = [1,1]
	if n == 1:
		return [1]
	elif n == 2:
		return [1,1]
	elif n < 1:
		return "Undefined!"
	else:
		for i in range(0,n-2):
			newnum = fibseq[-1]+fibseq[-2]
			fibseq.append(newnum)
		return fibseq
	
	
