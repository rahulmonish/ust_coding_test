student=[[" ",0,0,0],
[" ",0,0,0],
[" ",0,0,0],
[" ",0,0,0],
[" ",0,0,0],
[" ",0,0,0],
[" ",0,0,0],
[" ",0,0,0],
[" ",0,0,0],
[" ",0,0,0]]

for i in range(2):
        student[i][0]= input("enter the name")
        student[i][1]= int(input("enter mark1"))
        student[i][2]= int(input("enter mark2"))
        student[i][3]= int(input("enter mark3"))

for i in range(2):
    print("name : ",student[i][0],"\t \t mark1: ",student[i][1],"\t \t mark2 : ",student[i][2]," \t \t mark3 : ",student[i][3])

avg_mark1=0
avg_mark2=0
avg_mark3=0
for i in range(2):
    avg_mark1+= student[i][1]

    avg_mark2+= student[i][2]

    avg_mark3+= student[i][3]

print("\nmean \nsubject 1: ",avg_mark1/2,"\t \t subject 2 :",avg_mark2/2, " \t \t subject 3: ",avg_mark3/2)

for i in range(2):
    total= (student[i][1]+student[i][2]+student[i][3])/3
    if(total>90):
        print(student[i]," = A+")
    if(total<90 and total >80):
        print(student[i]," = A")
    if(total>70 and total<80):
        print(student[i]," = B+")
    if(total>60 and total<70):
        print(student[i]," = B")
    if(total>50 and total<60):
        print(student[i]," = C")
    if(total<50):
        print(student[i]," = D")
