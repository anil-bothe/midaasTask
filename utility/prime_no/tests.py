import time
from fast_prime import prime_generator as getFastPrimeNo
from gen_prime import prime_generator as getPrimeNo

print("""
Welcom to prime number generators.
There are two strategies 
Please Enter CMD:

F - Fast 
N - Normal  

""")

cmd = input('Enter cmd: ').upper()

if cmd == 'F':
    try:
        x = int(input(('Enter start integer :> ')))
        y = int(input(('Enter end integer :> ')))
        
        start_time = time.perf_counter()
        result = getFastPrimeNo(x, y)
        total_time = time.perf_counter() - start_time

        print(result)
        print('\nExecution time is %f' % total_time )
    except Exception as e:
        print(", ".join(i for i in e.args))

elif cmd == 'N':
    try:
        x = int(input(('Enter start integer :> ')))
        y = int(input(('Enter end integer :> ')))
        
        start_time = time.perf_counter()
        result = getPrimeNo(x, y)
        total_time = time.perf_counter() - start_time
        
        print(result)
        print('\nExecution time is %f' % total_time )
    except Exception as e:
        print(", ".join(i for i in e.args))

else:
    print('Please Enter valid cmd!')
