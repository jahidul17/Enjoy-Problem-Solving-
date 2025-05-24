
# def change(s):
#     if str.islower(s):
#         return str.upper()
#     else:
#         return str.lower()



# def swap_case(st):
#     return ''.join(map(change,st))

# --------------

# def swap_case(s):
#     str_swap=s.swapcase()
#     return str_swap

# --------------------

def swap_case(s):
    string = ""
    for i in s:
        # if i.isupper() == True:
        if i.isupper():
            string+=(i.lower())
        else:
            string+=(i.upper())

    return string


if __name__ == '__main__':
    s=input()
    result=swap_case(s)
    print(result)
