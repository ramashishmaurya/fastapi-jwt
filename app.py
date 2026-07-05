def creator():
    i = 1 
    while(i<=10):
        yield i 
        i = i+1 

x = creator()
print(next(x))
print(next(x))