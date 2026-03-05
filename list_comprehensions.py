# 1. Squares
#squares = [x**2 for x in range(1, 6)]
squares = []
for i in range(1,6):
    squares.append(i**2)
print(squares)


# 2. Even numbers
evens = [x for x in range(1,17) if x%2==0]
'''evens = []
for x in range(1,17):
    if x%2 == 0:
        evens.append(x)'''
print(evens)

'''
# 3. Uppercase names
names = ["marv", "kage", "shinobi"]
upper_names = [n.upper() for n in names]
print(upper_names)

# 4. Nested comprehension
matrix = [[i*j for j in range(1, 4)] for i in range(1, 9)]
print(matrix)

# 5. Conditional transform
numbers = [5, 12, 7, 20, 3]
labels = ["big" if n > 10 else "small" for n in numbers]
print(labels)
'''