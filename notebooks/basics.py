# /C:/class_folder/MATH3310_fall2025_InClassLab/notebooks/basics.py
1+2
x=2
y=3
z=x+y
print(z)
x="Hello,world!"
print(x)
l=[1,2,3,4,5]
print(l)
type(l)

# add 6
l.append(6)
print(l)

# relocate 4 with orange
l[3]="orange"
print(l)

# remove last element from the list
l.pop()
print(l)

# If 1 is less 2 print true or false
if 1<2:
    print("true")
else:
    print("false")

# print all even number from 1 to 10
for i in range(1,11):
    if i%2==0:
        print(i)

# Convert list l into a numpy array
import numpy as np
a=np.array(l)
print(a)
type(a)

# create a 2D numpy array
b=np.array([[1,2,3],[4,5,6]])
print(b)
b.ndim

# remove orange from the numpy array a
a=np.delete(a,3)
print(a)

# convert all elements of a to a float
a=a.astype(float)

# sum all elements in a
print(np.sum(a))
# taking the square root fo each element in a
print(np.sqrt(a))

# generate random data from a normal distribution
x=np.random.normal(0,1,1000)
x.shape

# add some random noise to the data
y=x+np.random.normal(0,0.1,1000)

# scatter plot of x and y
import matplotlib.pyplot as plt
plt.scatter(x,y) 
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatter plot of x and y")
plt.show()

# save plot as a png file
plt.savefig("scatter_plot.png")

#Hhaha