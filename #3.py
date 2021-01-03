case_number= int (input("케이스 갯수: ")) ;

for i  in range ((case_number)):
    student = [];
    student=list(map(int , input().split()));
    sum=0;
    for j in range(1,student.__len__()):
        sum= sum + student[j];
    average=sum/student[0];
    count=0;
    for k in range(1, student.__len__()):
        if(student[k]>average):
            count+=1;
    rate=round(count*100/student[0],3);

    print(rate);






