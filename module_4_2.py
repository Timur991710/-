x = 10


def test_function(x):
    y =  x + x


    def inner_function(s):
         z = s + s
         print(z)
    inner_function(10)

    return y

#inner_function(10)

rez = test_function(x)
print(rez)
