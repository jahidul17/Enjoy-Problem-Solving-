# if __name__ == '__main__':
#     n = int(input())
#     integer_list = map(int, input().split())
#     print(hash(integer_list))



if __name__ == '__main__':

    n = int(input())

    Tuple1 = (int, input().split())

    t = tuple(Tuple1)

    print(hash(t))