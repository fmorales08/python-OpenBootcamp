import functools
import operator


number_list = [5,65,94,55,444,82,3,11,152,132]
def odd(n):
  if n%2 != 0:
    return n

odd_list = list(filter(odd,number_list))

res_list  = functools.reduce(operator.add, odd_list)

print(res_list)