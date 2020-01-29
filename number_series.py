a=int(input("enter ur choice \n1.odd\n2.Even\n3.divisibleBy3\n4.divisibleBy5\n"))
if(a==1):
    for i in range(1,50):
        if i%2!=0:
            print(i)
elif(a==2):
    for i in range(1,50):
        if i%2==0:
            print(i)
elif(a==3):
    for i in range(1,50):
        if i%3==0:
            print(i)
elif(a==4):
    for i in range(1,50):
        if i%5==0:
            print(i)
else:
    print("incorrect choice")


'''
Sample Imput1
======
enter ur choice 
1.odd
2.Even
3.divisibleBy3
4.divisibleBy5
1

Sample Output1
======
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
>>>

Sample Imput3
======
enter ur choice 
1.odd
2.Even
3.divisibleBy3
4.divisibleBy5
3

Sample Output
======
3
6
9
12
15
18
21
24
27
30
33
36
39
42
45
48
>>> 

'''
