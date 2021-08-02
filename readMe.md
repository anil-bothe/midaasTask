# Midaas Telesoft Pvt Ltd.

This project is help you to generates prime number series.
Just download and install packages from requirement.txt

## Please go through following steps :    
    1. python manage.py makemigrations app
    2. python manage.py migrate
    3. python manage.py createsuperuser
    4. python manage.py runserver

## Important links
1. login/register new user
    - http://127.0.0.1:8000/midaas/login/
    - Use POST method 
    - Pass username and password in body/json
    - You will get token

2. Use token for each request

3. Get all primes number records
    - http://127.0.0.1:8000/midaas/prime-no/

4. Check prime no series
    - http://127.0.0.1:8000/midaas/prime-no/
    - Use POST Method
    - Pass algo_id, start_no and end_no in body/json
    - You will get result
