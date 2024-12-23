# numbers  = [1, 1 , 1 , 1, 8]
#
# for number in numbers:
#     value = ''
#     for count in range(number):
#         value += 'x'
#     print(value)
#
#
#     # output   ;
#     # x
#     # x
#     # x
#     # x
#     # xxxxxxxxx
#
#
#
# names = ['Bhathiya', 'Prasad', 'Maleesha', 'Chris', 'Dewdini']
# print(names[0])

numbers  = [100 ,  20900 , 2349 , 1000 , 999]
max_number = 0
for number in numbers:
    if number > max_number:
        max_number = number
    else:
        max_number = max_number
print(f"Max Number" ,  max_number)