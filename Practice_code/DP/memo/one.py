class Fibo:
    def find_num(self, num):
        if num == 0:
            return 0
        elif num <= 2:
            return 1
        else:
            return self.find_num(num - 1) + self.find_num(num - 2)

fibo = Fibo()
print(fibo.find_num(10))
