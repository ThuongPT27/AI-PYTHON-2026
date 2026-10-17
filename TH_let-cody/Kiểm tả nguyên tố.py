import sys

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    
    for i in range(1, t + 1):
        if i < len(input_data):
            s = input_data[i]
            
            last_4_digits = s[-4:]
            val = int(last_4_digits)
            if is_prime(val):
                print("YES")
            else:
                print("NO")

if __name__ == '__main__':
    main()
