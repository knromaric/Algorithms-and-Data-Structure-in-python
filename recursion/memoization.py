
'''
    Implement factorial Using Memoization
'''

# factorial_memo = {}
# def factorial(k): 
#     if k < 2: 
#         return 1
    
#     if not k in factorial_memo: 
#         factorial_memo[k]= k * factorial(k-1)

#     return factorial_memo[k]


# print(factorial(4))


class Memoize:
    def __init__(self, func): 
        self.func = func
        self.memo = {}

    def __call__(self, *args): 
        if not args in self.memo: 
            self.memo[args] = self.func(*args)
        
        return self.memo[args]


def factorial(k): 
    if k < 2: 
        return 1

    return k * factorial(k - 1)


fact = Memoize(factorial)

print(fact(5))