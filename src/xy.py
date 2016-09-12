import pylab
import numpy as np

xy=open("../data/xy.dat", "r")

#initialise empty lists for x and y 
x = []
y = []


while True:     # keeps looping until breaks out
    try:        #trys until reaches an exception
        #read line
        line = xy.readline()

        #split into two separate lists: x and y
        x_and_y = line.split()

        # If we do not have 2 words then it must be blank lines at the end of the file.
        if len(x_and_y) != 2:
            break    #exits loop
    except:
        
        # If we failed to read a line then we must have got to the end.
        break    #exits loop

    
    #append x and y where x value is the first column and y is second column
    #save these values as floats- if this is not possible it will go to except
    x.append(float(x_and_y[0]))
    y.append(float(x_and_y[1]))


#convert x and y lists to numpy arrays

x = np.array(x)
y = np.array(y)

pylab.plot(x,y)
pylab.xlabel("x")
pylab.ylabel("y")
pylab.show()

print "Maximum x: ",max(x)
print "Maximum y: ", max(y)
