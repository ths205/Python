#import plotly.plotly as py

#import plotly.graph_objs as go

#Creates a bar chart of the frequency of letters through a resume

import matplotlib.pyplot as plt

import numpy as n


a=0
b=0
c=0
d=0
e=0
f=0 
g=0
h=0
i=0
j=0
k=0
l=0
m=0
n=0
o=0
p=0
q=0
r=0
s=0
t=0
u=0
v=0
w=0
x_1=0
y_1=0
z=0

for line in open("programmer resume.doc"):

	for li in line:

		if li=='a':
			a=a+1

		elif li=='b':
		    b=b+1

		elif li=='c':
		    c=c+1

		elif li=='d':
		    d=d+1

		elif li=='e':
		    e=e+1

		elif li=='f':
		    f=f+1

		elif li=='g':
		    g=g+1

		elif li=='h':
		    h=h+1

		elif li=='i':
		    i=i+1

		elif li=='j':
		    j=j+1

		elif li=='k':
		    k=k+1

		elif li=='l':
		    l=l+1

		elif li=='m':
		    m=m+1

		elif li=='n':
		    n=n+1

		elif li=='o':
		    o=o+1

		elif li=='p':
		    p=p+1

		elif li=='q':
		    q=q+1

		elif li=='r':
		    r=r+1

		elif li=='s':
		    s=s+1

		elif li=='t':
		    t=t+1

		elif li=='u':
		    u=u+1

		elif li=='v':
		    v=v+1

		elif li=='w':
		    w=w+1

		elif li=='x':
		    x_1=x_1+1

		elif li=='y':
		    y_1=y_1+1 

		elif li=='z':
		    z=z+1

print a
print b

y_axis=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x_1,y_1,z]

#x_axis=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

fig=plt.figure()

ax=fig.add_subplot(111)

ind=range(26)

width=1

rect1=ax.bar(ind, y_axis, width, color='green')

ax.set_xlim(-width, len(ind)+width)

ax.set_ylim(0,500)

ax.set_ylabel('Frequency of letters')

x_axis=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

ax.set_xticks(ind)

xticksNames=ax.set_xticklabels(x_axis)

plt.setp(xticksNames, rotation=0, fontsize=10)

plt.show()
