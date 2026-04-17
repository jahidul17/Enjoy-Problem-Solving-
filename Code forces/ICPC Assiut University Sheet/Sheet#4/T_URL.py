url=input()
second_part=url.split('?')[1] #here 1 means second part after ?
# print(second_part)
params=second_part.split('&')
for param in params:
    key_value=param.split('=')
    key=key_value[0]
    value=key_value[1]
    print(f'{key}: {value}')

