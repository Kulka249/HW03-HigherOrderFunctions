def fun_map(func_1, func_2, L):
     return list(map(lambda x: func_1(x[1]) if (x[0] % 3 == 0) else func_2(x[1]), enumerate(L)))

def compose_map(func_1, func_2, L):
    return list(map(lambda x: func_2(func_1(x)), L))

def compose(func_1, func_2):
    def ret_fun(i):
        return func_1(func_2(i))
    return ret_fun

def repeater(fun, num_repeats):

    def ret_fun(x):
        for i in range(len(fun)):
            j = 0
            while j < num_repeats[i]:
                x = fun[i](x)
                j += 1
        return x
    return ret_fun

if __name__ == '__main__':

    def test1(x):
        return x * 3

    def test2(x):
        return x - 1

    data = [2,4,6,8,10,10,-3,-6,-7]

    # Testing the fun_map function
    print(fun_map(test1, test2, data)) # Calling the fun_map function with function test1 or test2 depending on index in list data where the list data is the argument

    # Testing the compose_map function
    print(compose_map(test1, test2, data)) # Calling the compose_map function with functions test1, test2 and the list data as the argument

    print(compose_map(test2, test1, data)) # Calling the compose_map function with functions test2, test1 and the list data as the argument (order of function input changed)

    # Using the compose function with functions test1 and test2 as arguments and returning its value to f1
    f1 = compose(test1, test2)

    # Running f1 with i=4
    print(f1(4))

    # Applying f1 on to each value in the list data
    print(list(map(f1, data)))

    # Using the compose function with functions test2 and test1 as arguments and returning its value to f2
    f2 = compose(test2, test1)

    # Running f2 with i=4
    print(f2(4))

    # Applying f2 on to each value in the list data
    print(list(map(f2, data)))

    # Testing the repeater function that with the function test1 with different num_repeats argument.
    z = repeater([test1, test2], [0 ,0])
    once = repeater([test1, test2], [1, 1])
    twice = repeater([test1, test2], [2, 2])
    thrice = repeater([test1, test2], [3, 3])

    print("repeat 0 times: {}".format(z(5)))
    print("repeat 1 time: {}".format(once(5)))
    print("repeat 2 times: {}".format(twice(5)))
    print("repeat 3 times: {}".format(thrice(5)))
