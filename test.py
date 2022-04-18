# string = '0,0,0,0,0,0,Irritable bowel syndrome (IBS),0,0,0,0,0,0,0,0'

# cause = string.split(',')
# data_cause = []
# for i in range(len(cause)):
#     if cause[i] != '0':
#         data_cause.append(cause[i])

# print(data_cause)

listen = ['Helicobacter', 'Hyperacidity', 'Candidiasis', 'Irritable bowel syndrome (IBS)', 'QQQQ', 'QQQQ', 'Hyperacidity']

new_list = []
for item in listen:
    if listen.count(item) >= 2:
        new_list.append(item)

print(new_list)
