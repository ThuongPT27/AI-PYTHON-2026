text=input("Nhập đoạn văn: ")
text=text.replace("!","")
text=text.replace(",","")
text=text.replace(".","")
text=text.replace("?","")
word=text.split()
vocab={}
for i in word:
    if i in vocab:
        vocab[i] +=1
    else:
        vocab[i] = 1
result = sorted(vocab.items(), key=lambda x: x[1], reverse=True)
for i, count in result:
    print(i, ":", count)
