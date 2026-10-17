import sys

def is_valid_ipv4(ip_str):
    parts = ip_str.split('.')
    if len(parts) != 4:
        return "NO"
        
    for part in parts:
        if not part or not part.isdigit():
            return "NO"
        if len(part) > 1 and part[0] == '0':
            return "NO"
        val = int(part)
        if val < 0 or val > 255:
            return "NO"
            
    return "YES"

def main():
    line = sys.stdin.readline()
    if not line:
        return
    t = int(line.strip())
    for _ in range(t):
        ip_str = sys.stdin.readline().strip()
        print(is_valid_ipv4(ip_str))

if __name__ == '__main__':
    main()
