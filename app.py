

def decorator(func):
    def wrapper():
        print('request is just initiared right ')
        func()
        print('payment is completed')
    return wrapper()

def hello():
    print('this is steps where all logic and writtens ')

app = decorator(hello)
#print(app)

def ashish(**kwargs):
    print(kwargs)

#print(ashish(name="ashsih" , age=12))


def generator():
    try:
        for i in range(1 ,3):
            yield i 
    except ValueError :
        print('there is an error here righ')
    finally:
        print('program is completed now ')

b = generator()
print(next(b))
print(next(b))