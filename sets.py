# Creating a set
my_set = {1, 2, 3, 4}

print(my_set)

# Adding an element
my_set.add(5)
print(my_set)

# Remove an element
my_set.remove(2)
print(my_set)

# Membership testing
print(2 in my_set)
print(3 in my_set)

# Sets 
# union (combining all into 1 set), intersection (whatever both sets have), 
# difference () - creates a new set all of these operations
set_a = {1,2,3}
set_b = {3,4,5}

# Union defaults ascending
union_value = set_a.union(set_b)
print(union_value)

# Intersection
intersection_value = set_a.intersection(set_b)
print(intersection_value)

# Difference what are the remainder elements (intersection is left out)
difference_value = set_a.difference(set_b)
print(difference_value)