# ========	
# ASKISI-1
# ========	

i=0
listword=[]
listlength=[]


f = open('Sample.txt')
for word in f.read().split():
    print( "Word [%5d] : [%32s]  length: %d" %(i , word , len(word)) )
    listword.append(word)
    listlength.append(len(word))
    i=i+1

for k in range(5):
    i  = max(listlength)
    j  = listlength.index(max(listlength))
    s1 = listword[j]
    s2 = listword[j][::-1]
    s3 = s2
    
    for char in 'aAeEiIoOuUyY':
        s3=s3.replace(char,'')

    
    print( "Max length [%2d]  at position [%3d] words: [%s]=>[%s]=>[%s]"  %(i, j, s1 , s2 , s3 ) )
    del listlength[j]
    del listword[j]
    




