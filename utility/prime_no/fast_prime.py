import time

def prime_generator(x:int, y:int) -> list:
    """
    ##########################################
    # Algo: Sieve of Eratosthenes 
    ##########################################
    'x' is starting point
    'y' is ending point
    """
    try:
        p = 2 # initialize
        prime_no = [i for i in range(y + 1)]
        
        # before x make zero
        for i in range(x):
            prime_no[i] = 0

        while p*2 <= y:
            if y != 0:
                for i in range(p*2, y+1, p):
                    # multiplication of 2,3,4...
                    prime_no[i] = 0
            p += 1
        
        return [i for i in prime_no if i != 0]
    except Exception as e:
        return ', '.join(i for i in e.args)



if __name__ == '__main__':
    st = time.perf_counter()
    try:
        x = int(input(('Enter start integer :> ')))
        y = int(input(('Enter end integer :> ')))
        result = prime_generator(17, 23)
    
        print(result)
    except Exception as e:
        print(", ".join(i for i in e.args))
    tt = time.perf_counter() - st
    print('\nExcution time is %s' % tt)
