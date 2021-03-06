import copy
import os
import sys
from copy import deepcopy

steps = list()


def quicksort(nums, fst, lst, key=0):
    try:
        p = 0
        s = 0

        if fst >= lst: return

        i, j = fst, lst
        pivot = nums[fst][key]

        while i <= j:
            s += 1
            while nums[i][key] < pivot:
                i += 1
                s += 1
            while nums[j][key] > pivot:
                j -= 1
                s += 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                steps.append(copy.copy(nums))
                i, j = i + 1, j - 1
                s += 1
                p += 1
        quicksort(nums, fst, j, key)
        quicksort(nums, i, lst, key)

        return [p, s, steps]
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno, e)


def vst(nums, n: int, by=0):
    try:
        p = 0
        s = 0
        steps = list()

        for i in range(2, n):
            if nums[i][by] < nums[i - 1][by]:
                rab = nums[i]
                j = i - 1
                s += 1
                while j > 0 and rab[by] < nums[j][by]:
                    nums[j + 1] = nums[j]
                    steps.append(copy.copy(nums))
                    j = j - 1
                    s += 1
                    p += 1
                nums[j + 1] = rab
        return [p, s, steps]
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno, e)
