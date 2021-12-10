#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# I predict output: 5
# Correct :)


#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# I predict output: ERROR
# Correct :)

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# I predict output: 5
# Correct :)

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# I predict output: 5, 10
# Incorrect :( 5 (only)... I see why.


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# I predict output: NO OUTPUT
# Incorrect :( 5 (only)... Have to go back to this one...


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
# I predict output: 3,5
# Correct :)

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# I predict output: 25
# Correct :)

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# I predict output: 100
# Incorrect :): 100, 10 (I see why.)


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# I predict output: 7,14, 21
# Correct :)

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# I predict output: 8,10
# Incorrect :(   8 only... why???


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# I predict output: 500, 500, 300, 500
# Correct :)

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# I predict output: 500, 500, 300, 300
# Incorrect :(    500, 500, 300, 500  hmmm...

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# I predict output: 500, 500, 300, 300
# Correct :)   OK, now I see...

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# I predict output: 1, 3, 2
# Correct :)

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# I predict output: 1, 10, 3, 5
# Correct :)