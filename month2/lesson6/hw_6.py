class Sum:
    def __init__(self, numbers: list, desired_sum: int):
        self.numbers = numbers
        self.desired_sum = desired_sum

    def index(self):
        for i in range(len(self.numbers)):
            for j in range(i + 1, len(self.numbers)):
                if (self.numbers[i] + self.numbers[j]) == self.desired_sum:
                    return (i, j)

    def __str__(self):
        return f"List of number: {self.numbers}\n" \
               f"Desired sum: {self.desired_sum}\n"


num = Sum(numbers=[2, 4, 8, 5, 7], desired_sum=11)
print(num)
print(num.index())
