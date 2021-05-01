def chat():                                              #chat라는 함수 설정
    print("철수: 안녕? 넌 몇 살이니?")                     
    print("영희; 나? 나는 20살이야","\n")                 #문자열 2개 출력후 한줄 공백

chat()                                                   #chat함수 실행

def chat(name1, name2, age):                             #함수에 넣고자 하는 인자 설정
    print("%s: 안녕? 넌 몇 살이니?" %name1)
    print("%s: 나? 나는 %d" %(name2, age) + "살이야!","\n") #인자가 대입된 문자열 2개 출력후 한줄 공백

chat("A","B", 10)                                        #인자 대입

chat("C","D", 20)                                        #인자 대입