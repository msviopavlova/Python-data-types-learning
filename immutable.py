# result = True
# another_result = result
# print(id(result))
# print(id(another_result))
# result = False
# print(id(result))
# since bool is immutable pythonrebound the var to a new value

# we ve attached the name result to a new value

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result+="ish"
print(id(result)) # now the result has a different ID
print(id(another_result))
# because strings are immutable, python couldn't change the string
#instead it created a new string and bound the name RESULT to a NEW string


