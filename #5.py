term = input();
term = term.upper();
count=0;
max=0;
for i in range (term.__len__()):
    count = 0;
    for j in range (i+1, term.__len__()):
        if term[i]== term[j] :
            count += 1;
    if max==count :
        max_term='?';
    if count > max:
        max_term = term[i];
        max =count;
    if max==0:
        max_term = term[i];
        if max == count:
            max_term = '?';

print(max_term);



