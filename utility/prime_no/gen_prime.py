import time

def is_prime(number):
    if number <= 1:
        return False
    
    for x in range(2, number//2):
        # if number is divisble by x
        if not number % x:
            return False
    return True

def prime_generator(x:int, y:int) -> list:
    """
    ++++++++++++++++++++++++++++++++++++++++++
    This is Prime Number Generator
    ++++++++++++++++++++++++++++++++++++++++++
    """
    try:
        return [i for i in range(x, y+1) if is_prime(i)]
    except Exception as e:
        msg = ', '.join(i for i in e.args)
        return msg


if __name__ == '__main__':
    start_time = time.perf_counter()
    try:
        x = int(input(('Enter start integer :> ')))
        y = int(input(('Enter end integer :> ')))
        
        result = prime_generator(x, y)
        
        print(result)
    except Exception as e:
        print(", ".join(i for i in e.args))
        
    total_time = time.perf_counter() - start_time
    print('\nExecution time is %s' % total_time)
    