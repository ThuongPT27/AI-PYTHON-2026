def max_tc(ds):
    if not ds:
        return None 
        
    max_val = ds[0]
    for num in ds:
        if num > max_val:
            max_val = num
    return max_val
  
a=list(map(int,input().split()))
print(max_tc(a))
