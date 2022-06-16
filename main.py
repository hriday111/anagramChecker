primes={
    'a':2,
    'b':3,
    'c':5,
    'd':7,
    'e':11,
    'f':13,
    'g':17, 
    'h':19,
    'i':23,
    'j':29,
    'k':31,
    'l':37,
    'm':41,
    'n':43,
    'o':47,
    'p':53,
    'q':59,
    'r':61,
    's':67,
    't':71,
    'u':73,
    'v':79,
    'w':83,
    'x':89,
    'y':97,
    'z':101,
}

input_word=input("Enter a word: ")
input_word2=input("Enter a word2: ")
base1=1
base2=1
for i in input_word:
    base1=base1*primes[i]
for j in input_word2:
    base2=base2*primes[j]
if base1==base2:
    print("true")
else:
    print(base1,base2)