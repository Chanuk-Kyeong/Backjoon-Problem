N = int(input("숫자:"));
c=' ';
c=c*(N-1);
a="*";
for i in range(0,N) :
    c=c+a;
    a=a+"*";
    print(c);
    c=' ';
    c=c*(N-2-i);