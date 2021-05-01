# 블리안 : boolean - 조건에 따라서

x = True                                        #변수 x
y = False                                       #변수 y

print(x), print(y)                              #변수 x,y 출력
print("\n")                                     #공백행

a = 3                                           #변수 a
b = 4                                           #변수 b

if a > b :                                      #변수 a가 변수 b보다 크다면
    print("a가 크다.")                           #진실일 경우 출력
print("False이기 때문에 출력이 안된다.", "\n")    #거짓일 경우 출력

c = 3                                           #변수 c

if c > 5 :                                      #변수 c가 5보다 크면 Hello 출력
    print("Hello","\n")
elif c == 3 :                                   #변수 c가 3이면 Bye 출력
    print("bye","\n")
else:                                           #그게 아니라면 Hi출력
    print("Hi","\n")