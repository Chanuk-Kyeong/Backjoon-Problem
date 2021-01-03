def unself_number(N):
    unself_number_array=[];
    all_number_array=[];
    for i in range(N):
        all_number_array.append(i);
    for a in range (0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    sum = a+b+c+d;
                    number=str(a)+str(b)+str(c)+str(d);
                    number=int(number);
                    result=sum+number;
                    if result <N :
                        unself_number_array.append(result);
                        unself_number_array = list(set(unself_number_array));
                        unself_number_array.sort();
    for j in range(unself_number_array.__len__()):
        all_number_array.remove(unself_number_array[j]);
    for k in range(all_number_array.__len__()):
        print(all_number_array[k])
unself_number(100)