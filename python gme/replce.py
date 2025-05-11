# def list_values():
#     ldst = []
#     for i in range(5):
#         num = int(input('enter values 1 to 12'  ))
#         ldst.append(num)
#     for s in range(len(ldst)):
#         if ldst[s] > 10:
#             ldst[s] = 10
#     print(ldst)

# list_values()

def remove_item(lst, item):
    lst = [1, 2, 3, 4, 5]
    lst.remove(item)
    return lst
print(remove_item(list, 3))




User_list = []
User_list1 = []

for  i in range(3):
    user_input = input('enter words ')
    User_list.append(user_input)
for x in range(len(User_list)):
     User_list1.append(User_list[x][1:])
print(User_list1)



    