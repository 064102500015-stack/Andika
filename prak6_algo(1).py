import math 
def is_prime(number):

    if number <= 1:
        return False
    limit = int(math.sqrt(number)) + 1
    for i in range(2, limit):
        if number % i == 0:
            return False 
            
    return True 

def run_program():
    
    try:
        angka = int(input("Masukkan angka: "))

        if is_prime(angka):
            print(f"{angka} adalah bilangan Prima")
        else:
            print(f"{angka} bukanlah bilangan Prima")
            
    except ValueError:
        print("Input tidak valid. Harap masukkan bilangan bulat.")

if __name__ == "__main__":
    run_program()