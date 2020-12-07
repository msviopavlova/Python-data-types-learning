shopping_list = ["milk",
                  "pasta",
                  "eggs",
                  "spam",
                  "bread",
                  "rice"
                  ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"] # we have to use square brackets to add it
print(shopping_list)

print(id(shopping_list)) # the ID remains the same after thanging the list

#python added an item to the existing list without creating a new one.
print(another_list) #both objects now have cookies added to it, they still are equal


a=b=c=d=e=f=another_list # chain assignment
#we havent copied ne list we just bound a name to it

print(a)

print("Adding cream")

b.append("cream") # appending is adding

print(c)
print(d)


print(f)

#when we look at lists that contain lists multiple variables can be equal/useful






