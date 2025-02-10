# simple interst calculation

def simple_intrest(p, n, r):
    i = (p*n*r)/100
    amt = p + i
    return{"intrest": i,"amoun": amt}
# take input from user in consol
p = float(input("Please enter Principle in INR"))
n = int(input("Please enter Number of years: "))
r = float(input("Please enter rate of intrest in %p.a. :"))

#calculate interst and amount
results = simple_intrest(p,n,r)

#print the results
print(results)
