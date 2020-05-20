while True :

 f = input("계산하고 싶은 수식을 입력하시오.(숫자 연산자 숫자 형식) ")
 f=f.split(" ")
 a=f.pop(0)
 b=f.pop(1)

 if('+' in f) :
    s=int(a)+int(b)
    print("답은 ", s, "입니다.")
 elif('-' in f) :
    s=int(a)-int(b)
    print("답은 ", s, "입니다.")
 elif('/' in f) :
    s=int(a)/int(b)
    print("답은 ", s, "입니다.")
 elif('*' in f) :
    s=int(a)*int(b)
    print("답은 %lf입니다." %s)
 else : 
    print("잘못 입력하셨습니다.")
    continue;

 g=input("다시 하고 싶으면 c, 끝내고 싶으면 e를 입력하시오. ")
 if(g=='c') :
     continue;
 elif(g=='e') :
     break;
