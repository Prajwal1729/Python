
# a = [23,90,200,56]

# a.remove(1)
# print(a)

# my_dict = {'name':'max'}

# x = -5
# # if x < 0:
# #     raise Exception("x should b positive")
# assert(x>=0), 'x is not positive'

# try:
#     b = 10/0
# except Exception as e:
#     print(e)



# try:
#     a = 5/0
#     b = a + "90"
# except Exception as e:
#     print(e)
# except TypeError as e:
#     print(e)

# else:
#     print("Everything is fine")

# finally:
#     print("Cleaning up")


class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __init__(self,msg,val):
        self.msg = msg
        self.val = val



def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high")
    if x < 5:
        raise ValueTooSmallError("value is too small",x)

try:
    # test_value(900)
    test_value(3)
except ValueTooHighError as e:
    print(e)

except ValueTooSmallError as e:
    print(e)


