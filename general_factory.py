# def greeting_function(name):
#     return (f'hello {name}')

# create a function that takes 1 string arg
# returns the formatted string (removes the empty spaces)

def return_formated_name(name):
    return name.title().strip()
name = return_formated_name("     mr.  ")
expected_output = "Mr."
print(return_formated_name(name) == expected_output)

