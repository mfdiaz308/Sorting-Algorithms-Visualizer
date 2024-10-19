import time
from random import randint

def bubble(data: list[int], drawData, timer: float) -> None:
    n: int = len(data)

    for i in range(n):
        for j in range(n-1-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1],data[j]

                # If swapped color turns green, else stays red
                drawData(data, ['Green' if x==j+1 else 'Red' for x in range(len(data))])
                time.sleep(timer)

    # Sorted = green
    drawData(data, ['Green' for x in range(len(data))])

def insertion(data: list[int], drawData, timer: float) -> None:
    for i in range(1, len(data)):
        key_item: int = data[i]
        j: int = i - 1
        while j >= 0 and data[j] > key_item:
            data[j + 1] = data[j]
            j -= 1
            drawData(data, ['Green' if x==j+1 else 'Red' for x in range(len(data))])
            time.sleep(timer)
        data[j + 1] = key_item

    drawData(data, ['Green' for x in range(len(data))])

# TODO: merge sort
# def merge(data: list[int], drawData, timer: int) -> None:



# def quick_sort(data: list[int], section: list[int], drawData, timer: float) -> list[int]:
#     if len(section) <= 1:
#         return section
#     else:
#         pivot: int = section[randint(0,len(section)-1)]
#         # pivot: int = max(data)

#         left: list[int] = [d for d in section if d < pivot]
#         middle: list[int] = [d for d in section if d == pivot]
#         right: list[int] = [d for d in section if d > pivot]

#         print(f'{pivot=}\n{left=}\n{middle=}\n{right=}')
        
#         # drawData(data, ['Green' for x in range(len(data))])
#         drawData(data, ['Green' if x==j+1 else 'Red' for x in range(len(data))])
#         time.sleep(timer)

#         return quick_sort(data, left, drawData, timer) + middle + quick_sort(data, right, drawData, timer)

def partition(data: list[int], head: int, tail: int, drawData, timer: float) -> int:
    border: int = head
    pivot: int = data[tail]
    # pivot: int = data[randint(0,len(data)-1)]
 
    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(timer)
 
    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(timer)
 
            data[border], data[j] = data[j], data[border]
            border += 1
 
        drawData(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(timer)
 
    # swapping pivot with border value
    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(timer)
 
    data[border], data[tail] = data[tail], data[border]
 
    return border
 
 
# head  --> Starting index,
# tail  --> Ending index
def quick_sort(data: list[int], head: int, tail: int, drawData, timer: float) -> None:
    if head < tail:
        partitionIdx: int = partition(data, head, tail, drawData, timer)
 
        # left partition
        quick_sort(data, head, partitionIdx-1, drawData, timer)
 
        # right partition
        quick_sort(data, partitionIdx+1, tail, drawData, timer)
 
# Function to apply colors to bars while sorting:
# Grey - Unsorted elements
# Blue - Pivot point element
# White - Sorted half/partition
# Red - Starting pointer
# Yellow - Ending pointer
# Green - after all elements are sorted
 
# assign color representation to elements
 
 
def getColorArray(dataLen: int, head: int, tail: int, border: int, currIdx: int, isSwaping: bool =False) -> list[str]:
    colorArray: list[str] = []
    for i in range(dataLen):
        # base coloring
        if i >= head and i <= tail:
            colorArray.append('Grey')
        else:
            colorArray.append('White')
 
        if i == tail:
            colorArray[i] = 'Blue'
        elif i == border:
            colorArray[i] = 'Red'
        elif i == currIdx:
            colorArray[i] = 'Yellow'
 
        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'Green'
 
    return colorArray


# if __name__ == '__main__':
#     def quick_sort(data: list[int]) -> list[int]:
#         if len(data) <= 1:
#             return data
#         else:
#             pivot: int = data[randint(0,len(data)-1)]
#             # pivot: int = max(data)

#             left: list[int] = [d for d in data if d < pivot]
#             middle: list[int] = [d for d in data if d == pivot]
#             right: list[int] = [d for d in data if d > pivot]

#             print(f'{pivot=}\n{left=}\n{middle=}\n{right=}')

#             return quick_sort(left) + middle + quick_sort(right)
        
    # print(quick_sort([2,7,4,19,1,3,2]))
