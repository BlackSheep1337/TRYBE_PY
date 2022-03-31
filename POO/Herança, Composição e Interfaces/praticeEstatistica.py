from collections import Counter


class Estatistica:
    @classmethod
    def media(cls, numbers):
        return sum(numbers) / len(numbers)

    @classmethod
    def mediana(cls, numbers):
        numbers.sort()
        i = len(numbers) // 2
        if len(numbers) % 2 == 0:
            return (numbers[i - 1] + numbers[i]) / 2
        return numbers[i]

    @classmethod
    def moda(cls, numbers):
        number, times = Counter(numbers).most_common()[0]
        return f"{number} is the most comum, it appears {times} times"


statistic = Estatistica()

print(statistic.mediana([3, 4, 9, 12]))

print(statistic.media([2, 3, 4, 9, 12]))

print(statistic.moda([2, 3, 4, 9, 12, 2, 3, 12, 3, 3, 9, 23]))