#We'll convert the tuple to a set because it cant have duplicate elements.
original_tuple= (2,4,6,8,7,2,4,5,6,7,8,9,7,3,2,3,5,4)
print("The Original Tuple is " + str(original_tuple))
# Printing The original tuple in console
new_set = tuple(set(original_tuple))
print("The New Set after conversion is" + str(new_set))
