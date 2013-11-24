x=int(raw_input('Give me a number '))
for i in range(2,x):
    if x%i==0:
        x=False 
    else:
        x=True 
print x
