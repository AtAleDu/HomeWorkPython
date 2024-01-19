def func1(x):
    if x > 0:
        print(f"func1({x}) вызван")
        func2(x - 1)
    else:
        return

def func2(y):
    if y > 0:
        print(f"func2({y}) вызван")
        func1(y - 1)
    else:
        return

func1(3)
print("____________________________________________S")
func2(5)