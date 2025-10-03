a = 70

def func():
    global a
    a = 6
    print(a)

func()
print(a)