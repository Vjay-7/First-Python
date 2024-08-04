

# def sum_val(num, n):
#     if type(num[n]) is list():
#         total += 
# #   if not num:
# #     return 0
# #   return num[0]+ sum_val(num[1:])

# num=[1, 2, [3,4], [5,6]]
# n= len(num)
# print(sum_val(num))

#!~~~~~~~~~~~~~Factorial
# def factorial_num(num):
#     if num == 1:
#         return 1
#     return num * factorial_num(num-1)

# num= int(input())
# print(factorial_num(num))

#~~~~~~~~~Fibonacci

#~~~~~~~~~~Add tapad value
# def sum_int(num):
#     if num == 0:
#         return 0
#     return num%10 + sum_int(int(num/10))

#~~~~~~~~~Add by preceeded number by 2
# def sub_sum(num):
#     if num == 0:
#         return 0
#     return num + sub_sum(num-2)
# print(sub_sum(10))

#~~~~~~~~ Harmonic Sum
# def harmonic_sum(num):
#     if num == 1:
#         return 1
#     return (1/num)+ harmonic_sum(num-1)
# print(harmonic_sum(7))

#~~~~~~~ Exponent 
# def epo(base,expon):
#     if expon == 0:
#         return 1
#     return base * epo(base, expon-1)
# print(epo(3,1))

for i in range(1,7):
    print(i, end=',')