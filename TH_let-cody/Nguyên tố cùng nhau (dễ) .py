import sys
import math

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    start = 10**(k - 1)
    end = 10**k
    
    count = 0
    row = []
    for i in range(start, end):
        if math.gcd(i, n) == 1:
            row.append(str(i))
            count += 1
            
            if count == 10:
                print(" ".join(row))
                row = []
                count = 0
              
    if row:
        print(" ".join(row))

if __name__ == '__main__':
    main()
