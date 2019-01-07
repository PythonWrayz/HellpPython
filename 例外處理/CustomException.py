# 客製 Exception
class RayException(Exception):
    pass


def test():
    raise RayException("Hey 有錯")


test()
