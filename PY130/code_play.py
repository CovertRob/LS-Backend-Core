# Factory function example

def greeter(prompt):
    def add_greet(str_input):
        return prompt + str_input
    return add_greet

name = 'Robby'

say_hello = greeter('howdy ')
print(say_hello(name))

# lst = ['a', 'bb', 'ccccc', 'dd']
# new_lst = sorted(lst, key=len)
# print(new_lst)

# imperitive
# lst = ['one', 'two', 'three']
# new_lst = []
# for item in lst:
#     new_lst.append(item.title())

#   # declarative
# new_lst = map(str.title, lst)
# print(list(new_lst))