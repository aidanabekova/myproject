#структуры данных и алгоритмы


#алгоритм Bubble sort(пузырьковая сортировка)
# numbers = [3, 1, 81, 35, 22]
# def bubble_sort(numbers):
#     swapped = False
#     for i in range(len(numbers) - 1, 0, -1):
#         for j in range(i):
#             if numbers[j] > numbers[j + 1]:
#                 numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
#                 swapped = True
#         if swapped:
#                 swapped = False
#         else:
#             break
#     return numbers
#
#
# print(f"Sorted list: {bubble_sort(numbers=numbers)}")


#алгоритм Quick sort(быстрая сортировка)
numbers = [3, 1, 22, 35, 88]

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    element = numbers[0]
    left = list(filter(lambda num: num < element, numbers))
    center = [num for num in numbers if num == element]
    right = list(filter(lambda num: num > element, numbers))

    return quick_sort(left) + center + quick_sort(right)

print(f"Sorted list: {quick_sort(numbers)}")

