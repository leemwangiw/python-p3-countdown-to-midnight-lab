import time

def countdown(n):
    while n > 0:
        print(f'{n} SECOND(S)!')
        n -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(n):
    while n > 0:
        print(f'{n} SECOND(S)!')
        time.sleep(1)  # Pauses for 1 second
        n -= 1
    print("HAPPY NEW YEAR!")
#hhdhfff
