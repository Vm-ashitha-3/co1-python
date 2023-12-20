text="welcome to my youtube channel"
text_list=text.split()
count=0
for i in text_list:
    for j in text_list:
        if i==j:
            count+=1
    print(i,"-",count,"times")
    count=0
