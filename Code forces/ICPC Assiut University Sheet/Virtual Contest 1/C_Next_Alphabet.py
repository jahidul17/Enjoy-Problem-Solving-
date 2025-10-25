
c=input()

asc_int=ord(c)

if(asc_int>=97 and asc_int<=121):
    print(chr(asc_int+1))
elif(asc_int==122):
    print(chr(97))
