nn = len(x)
pp = 3 #number of paramters (changes based on model)
yfit = f(x,p0,p1,p2) #this calculates the model fitting function at the x 
yys = ((y-yfit)**2)/yerr**2 # this generates an array of the squared differ
chisqr = sum(yys)/(nn-pp) # compute reduced chi-squared
print(f'Reduced chi-squared = {chisqr:.3f}')
