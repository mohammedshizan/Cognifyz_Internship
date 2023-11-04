f=open ("Hello!.txt","r")
text=f.read().split()
print(text)
f.close()

word_count={}
for word in text:
    word=word.lower()
    word_count[word]=word_count.get(word,0)+1
    
    
for word, count in sorted(word_count.items()):
    print(f'{word}:{count}')
    
    
    
    
    
    
    
    
    
     



    


    