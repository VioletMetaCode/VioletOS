import sys
import numpy as np
a = [
1023,
995,
985,
971,
953,
930,
926,
921,
916,
909,
903,
897,
891,
885,
877,
869,
863,
856,
848,
839,
830,
822,
814,
805,
796,
785,
777,
768,
758,
747,
735,
726,
716,
705,
694,
682,
672,
661,
650,
638,
625,
615,
604,
593,
581,
568,
558,
547,
535,
524,
511,
501,
490,
479,
468,
456,
446,
436,
425,
415,
403,
394,
385,
375,
365,
355,
346,
338,
329,
320,
310,
270,
235,
204,
177,
153,
132,
115,
100,
87,
76,
66,
58,
51,
44,
39,
0]
k=[
-50,
-40,
-35,
-30,
-25,
-20,
-19,
-18,
-17,
-16,
-15,
-14,
-13,
-12,
-11,
-10,
-9,
-8,
-7,
-6,
-5,
-4,
-3,
-2,
-1,
0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10,
11,
12,
13,
14,
15,
16,
17,
18,
19,
20,
21,
22,
23,
24,
25,
26,
27,
28,
29,
30,
31,
32,
33,
34,
35,
36,
37,
38,
39,
40,
41,
42,
43,
44,
45,
50,
55,
60,
65,
70,
75,
80,
85,
90,
95,
100,
105,
110,
115,
120,
130
]
# zero padding
d=[]
cnt = len(a)-1
nCnt = 0;
for i in range(0,1024):
  if i < a[cnt]:
    d.append(int(k[cnt+1]-(((k[cnt+1]-k[cnt])/(a[cnt]-a[cnt+1]-1))*nCnt)))
    # print(k[cnt+1]-k[cnt])
    # print(a[cnt]-a[cnt+1]-1)
    # print(k[cnt])
    # print("cnt"+str(cnt))
    # print(int(k[cnt+1]-(((k[cnt+1]-k[cnt])/(a[cnt]-a[cnt+1]-1))*nCnt)))
    nCnt+=1;    
  elif i == a[cnt]:
    d.append(k[cnt])
    cnt-=1
    nCnt = 1
  elif cnt == -1:
    d.append(0)
  else :
    print("error"+str(i))
    
print(d)

