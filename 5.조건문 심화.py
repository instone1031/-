x = 2                                                      #변수 x
y = 1                                                      #변수 y
z = 0                                                      #변수 z

if x > y :
    print("x는 y보다 크다.")                                #~라면
print("x가 y보다 크기 때문에 출력된다.","\n")

if not x < y :
    print("x보다 y가 크지 않다.")                            #~가 아니라면
print("not이 붙어서 True이기 때문에 출력된다.","\n")

if x > z and x > y :
    print("y가 z보다 크고 x가 y보다 크다.")                  #~와 ~라면
print("두가지 모두 맞으면 출력된다.","\n")

if z > y or x > y :
    print("z가 y보다 크거나 또는 x가 y보다 크다.")            #~ 또는 ~라면
print("두가지중 하나만 맞아도 출력된다.")
