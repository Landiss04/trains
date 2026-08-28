
number=200000
n1=1
n2=1
save=[]
zero_num_s=0
each_10=[]
count_till=0
for i in range(number):
    n3=n1+n2
    n1=n2
    n2=n3
    n_count=str(n3)
    save.append(n_count[-1])
    zero_num=len(n_count)-1
    if zero_num>zero_num_s:
        each_10.append([zero_num_s,count_till])
        count_till=0
        zero_num_s=zero_num
    count_till+=1
    #print(n3)


#print(save)
#print(count_till)
#print(each_10)
sums=0
for i in each_10:
    #print(i)
    sums+=i[1]
mean=sums/len(each_10)
#print(mean)
print(n3)
