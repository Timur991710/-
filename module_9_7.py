def is_prime(func):
    def prosto_1(*args):
        procto = func(*args)
        list = []
        for i in range(procto):
            i = i + 1
            if procto % i == 0:
                list.append(i)
        if len(list) > 2:
            return(f"Составное\n {procto}")
        else:
            return(f"Простое\n {procto}")


    return prosto_1

@is_prime
def sum_three(*args):
    x = 0
    for i in args:
        x +=i
    return x



result = sum_three(2, 3, 7)
print(result)