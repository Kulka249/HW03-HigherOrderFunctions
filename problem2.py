def stencil(data, f, width):
    stencil = []

    for i in range(len(data) - width + 1):
        stencil.append(f(list(map(lambda x: x[1], filter(lambda x: x[0] >= i and x[0] < i + width, enumerate(data))))))
        
    return stencil

def create_box(box):
    
    def box_filter(L):
        if len(box) != len(L):
            print(f"Calling box filter with the wrong length list. Expected length of list should be {len(box)}.")
            return 0

        b_sum = 0
        for i in range(len(box)):
            b_sum += box[i] * L[len(box) - i - 1]

        return b_sum

    return box_filter, len(box)


if __name__ == '__main__':
    # The block of code under the `if __name__ == '__main__':` statement is only executed when the script is run as the main program.
    # This block is not executed if the script is imported as a module.
    
    def mov_avg(L):
        # The `mov_avg` function takes in a list `L` and returns the moving average of its elements.
        return float(sum(L)) / 3
    
    # Define a function `sum_sq` that takes in a list `L` and returns the sum of the squares of the elements in `L`.
    def sum_sq(L):
        return sum([i ** 2 for i in L])
    
    data = [2,4,6,8,10,10,-3,-6,-7]
    
    print(stencil(data, mov_avg, 2))
    print(stencil(data, sum_sq, 5))
    
    # note that this creates a moving average!
    box_f1, width1 = create_box([1.0 / 4, 1.0 / 4, 1.0 / 4, 1.0/4])
    print(stencil(data, box_f1, width1))
    
    box_f2, width2 = create_box([-0.2, -0.3, 0.3, 0.2])
    print(stencil(data, box_f2, width2))
