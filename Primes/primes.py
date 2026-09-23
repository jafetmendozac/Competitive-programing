# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def is_prime(num: int) -> bool :
    if num <= 1: return False
    if num == 2: return True
    if num % 2 == 0: return False
    for i in range(2, int(num**0.5) +1, 2):
        if num % (i+2) == 0:
            return False
    return True
    

if(is_prime(5)):
    print("Es primo")
else:
    print("No es primo")
