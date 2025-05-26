import textwrap

def wrap(text,width):
    return textwrap.fill(text, width)

if __name__ == '__main__':
    text,width=input(),int(input())
    result=wrap(text,width)
    print(result)



