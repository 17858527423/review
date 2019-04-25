from timeit import Timer
from random import randint


# 冒泡排序：两两往右比较，找到最大的放到最右边,n,n-1,n-2
def bubbleSort(alist):
    """
    冒泡排序
    :param alist:列表
    :return:
    """
    n = len(alist)
    for j in range(n-1):
        # 如果没有改变，直接输出
        count = 0
        for i in range(0,n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if count == 0:
            return


# 选择排序：假设第一个是最小的，往右对比，
# 找到最小值，放到第一个，然后找第二个。。。n,n-1,n-2
def selectSort(alist):
    """
    选择排序
    :param alist:列表
    :return:
    """
    n = len(alist)
    for j in range(0, n-1):
        min_index = j
        for i in range(j+1,n):
            if alist[i] < alist[min_index]:
                alist[i],alist[min_index] = alist[min_index], alist[i]
                min_index = i


# 插入排序：从左往右，把第k个向左比较，放到适当位置,1,2,3,4
# 无序放到有序的列表
def insertSort(alist):
    """
    插入排序：第k个向左比较，放到适当位置
    :param alist:列表
    :return:
    """
    for i in range(len(alist)):
        for j in range(i,0,-1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]


# 希尔排序：定义步长，用插入排序，然后平分步长，插入排序
def shellSort(alist):
    n = len(alist)
    # 初始步长
    gap = n // 2
    while gap > 0:
        # 将步长进行排序
        for i in range(gap, n):
            # j = [gap, gap+1, gap+2, gap+3,...,n-1]
            j = i
            while j > 0:
                if alist[i] <= alist[i - gap]:
                    alist[j - gap], alist[j] = alist[j], alist[j - gap]
                    j -= gap
                else:
                    break
        # 将步长评分
        gap //= 2


# 把第一个放到中间正确位置，然后二分
def quickSort(alist, first, last):
    """快速排序"""
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        # 将high从右向左遍历
        # 如果有比中间值小，则和low互换
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        # 将low从左向右遍历
        # 如果有比中间值大，则和high互换
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_value
    quickSort(alist, first, low-1)
    quickSort(alist, low+1, last)


# 归并排序
def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    # left 采购归并排序后形成的有序的新的列表
    left_li = merge_sort(alist[:mid])
    # right 采购归并排序后形成的有序的新的列表
    right_li = merge_sort(alist[mid:])
    # 将两个有序的子序列合并为一个新的整数
    # merge(left,right)
    left_pointer, right_pointer = 0, 0
    result = []
    # 各自往右，依次把值按从小到大放入新的列表
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] <= right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result


def test1():
    a = [randint(1,100) for i in range(1000)]
    bubbleSort(a)


def test2():
    b = [randint(1, 100) for i in range(1000)]
    selectSort(b)


def test3():
    c = [randint(1, 100) for i in range(1000)]
    insertSort(c)


def test4():
    d = [randint(1, 100) for i in range(1000)]
    quickSort(d, 0, len(d)-1)



def test5():
    e = [randint(1,100) for i in range(1000)]
    shellSort(e)



def test6():
    f = [randint(1,100) for i in range(1000)]
    f = merge_sort(f)


if __name__ == '__main__':
    timer1 = Timer("test1()", "from __main__ import test1")
    print("bubbleSort:", timer1.timeit(1000))

    timer2 = Timer("test2()", "from __main__ import test2")
    print("selectSort:", timer2.timeit(1000))

    timer3 = Timer("test3()", "from __main__ import test3")
    print("insertSort:", timer3.timeit(1000))

    timer4 = Timer("test4()", "from __main__ import test4")
    print("quickSort:", timer4.timeit(1000))

    timer5 = Timer("test5()", "from __main__ import test5")
    print("shellSort:", timer5.timeit(1000))

    timer6 = Timer("test6()", "from __main__ import test6")
    print("mergeSort:", timer6.timeit(1000))

    # a = [4,1,8,3,5,6,2,9,7]
    # bubbleSort(a)
    # print(a)
    # b = [4, 1, 8, 3, 5, 6, 2, 9, 7]
    # selectSort(b)
    # print(b)
    # c = [4, 1, 8, 3, 5, 6, 2, 9, 7]
    # insertSort(c)
    # print(c)
    # d = [4, 1, 8, 3, 5, 6, 2, 9, 7]
    # quickSort(d,0,len(d)-1)
    # print(d)
    # e = [4, 1, 8, 3, 5, 6, 2, 9, 7]
    # shellSort(e)
    # print(e)
    # f = [4, 1, 8, 3, 5, 6, 2, 9, 7]
    # f = mergeSort(f)
    # print(f)



