import sys

# def test(**kwargs):
#     print(kwargs)
#     print(list(kwargs.keys())[0])
#     if list(kwargs.keys())[0] == 'size':
#         print('Получилось')
# # test(size=100)
# if __name__ == '__main__':

#     print(sys.argv[1], 'str=', 11 )
#     s = sys.argv[1]
#     ind = s.find('=')
#     kluch = s[: ind]
#     print(kluch, 'str=', 15)
#     znach = s[ind+1 :]
#     test(kluch = znach)

def test(*args):
    print(args)

# test(7,9)
if __name__ == '__main__':
    s = sys.argv[1]
    print(s)
    test(s)
