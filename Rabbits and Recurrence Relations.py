import matplotlib.pyplot as plt

#Dataset: Month = 29, Offspring = 4 per cycle

monthInput= 29
offspringInput = 4
childArr = [1]
monthArr = [1]

def fib(month, offsprings):
    parent, child = 1, 1
    for i in range(month-1):
        child, parent = parent, parent + (child*offsprings)
        childArr.append(child)
        monthArr.append(i)
    return child


x = fib(monthInput, offspringInput)
print(x)
print(childArr)

# Graph
plt.ylabel("Month")
plt.xlabel("Rabbits")
plt.plot(monthArr, childArr)
plt.show()


