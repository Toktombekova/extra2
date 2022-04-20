# nums = [1, 2, 3, 4, 5, 6, 7, 8]
#
# target = 8
# if target in nums:
#   print(f"{nums.index(target)}")
# else:
#     print(-1)

class Nums:
    _numbers_ = [1, 2, 3, 4, 5, 6, 7]

    def __init__(self, target):
        self.target = target

    def get(self):
        if self.target == 2:
            print(f"{self._numbers_.index(self.target)}")
        else:
            print(f"-1")


num = Nums(2)
num.get()
