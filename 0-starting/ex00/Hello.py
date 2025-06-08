ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# List: By index
ft_list[1] = "World!"

# Tuple: By default, we cannot edit a tuple. So we have to convert to a list
tmp = list(ft_tuple)
tmp[1] = "France!"
ft_tuple = tuple(tmp)

# Set
ft_set.remove("tutu!")
ft_set.add("Paris!")

# Dictionnary
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
