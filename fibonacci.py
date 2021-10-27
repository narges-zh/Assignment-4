n=int(input('enter n:'))
def f(x):
    if x==1:
      return 0 
    if x==2:
      return 1
    else:
      return f(x-1)+f(x-2)

def t(y):
    i=1
    while i<y:
        yield i  #return from a function
        i=i+1

for i in t(n+1):
    print(f(i))


