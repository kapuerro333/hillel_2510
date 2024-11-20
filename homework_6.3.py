lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2= [item for item in lst1 if isinstance(item, str)]
if lst2:
    print("New list created:", lst2)
else:
    print("No strings are displayed.")

print("Created list", lst2)