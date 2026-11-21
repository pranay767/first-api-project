def outer():
    count = 0
    def increase():
        nonlocal count
        count += 1
    def display():
        print(count)
    return [increase, display]

[increase, display]=outer()

for i in range(0,5):
    increase()
    display()

# [increase, display] = outer()
#
# increase()
# increase()
# increase()
# increase()
# increase()
# print(display())