def dem(ds):
    tan_suat = {}
    for i in ds:
        if i in tan_suat:
            tan_suat[i] += 1
        else:
            tan_suat[i] = 1
    return tan_suat
  
a=list(map(int,input().split()))
print(dem(a))
