import sys

def convert_base(n, b):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if n == 0:
        return "0"
        
    result = []
    while n > 0:
        result.append(digits[n % b]) 
        n //= b                       
    return "".join(reversed(result))

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    for _ in range(t):
        if idx < len(input_data):
            n = int(input_data[idx])
            b = int(input_data[idx+1])
            idx += 2
            print(convert_base(n, b))

if __name__ == '__main__':
    main()
