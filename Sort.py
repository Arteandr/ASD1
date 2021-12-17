from typing import List
from Row import Row


def quicksort(data: List[Row], left, right):
    try:
        sravn: int = 0
        perest: int = 0

        pivot: int
        l_hold: int = left
        r_hold = right
        pivot = int(data[left].id)
        while left < right:
            sravn += 1
            while int(data[right].id) >= pivot and left < right:
                right = right - 1
                sravn += 1
            if left != right:
                data[left].id = int(data[right].id)
                data[left].name = str(data[right].name)
                data[left].age = int(data[right].age)
                left = left + 1
                sravn += 1
                perest += 1
            while int(data[left].id) <= pivot and left < right:
                sravn += 1
                left = left + 1
            if left != right:
                data[right].id = int(data[left].id)
                data[right].name = str(data[left].name)
                data[right].age = int(data[left].age)
                right = right - 1
                sravn += 1
                perest += 1

        data[left].id = int(pivot)
        pivot = left
        left = l_hold
        right = r_hold
        if left < pivot:
            sravn += 1
            quicksort(data, left, pivot - 1)
        if right > pivot:
            sravn += 1
            quicksort(data, pivot + 1, right)

        return [sravn, perest]
    except Exception as e:
        print(e)


def quicksort_age(data: List[Row], left, right):
    try:
        sravn: int = 0
        perest: int = 0

        pivot: int
        l_hold: int = left
        r_hold = right
        pivot = int(data[left].age)
        while left < right:
            sravn += 1
            while int(data[right].age) >= pivot and left < right:
                right = right - 1
                sravn += 1
            if left != right:
                data[left].id = int(data[right].id)
                data[left].name = str(data[right].name)
                data[left].age = int(data[right].age)
                left = left + 1
                sravn += 1
                perest += 1
            while int(data[left].age) <= pivot and left < right:
                sravn += 1
                left = left + 1
            if left != right:
                data[right].id = int(data[left].id)
                data[right].name = str(data[left].name)
                data[right].age = int(data[left].age)
                right = right - 1
                sravn += 1
                perest += 1

        data[left].age = int(pivot)
        pivot = left
        left = l_hold
        right = r_hold
        if left < pivot:
            sravn += 1
            quicksort_age(data, left, pivot - 1)
        if right > pivot:
            sravn += 1
            quicksort_age(data, pivot + 1, right)

        return [sravn, perest]
    except Exception as e:
        print(e)


def quicksort_name(data: List[Row], left, right):
    try:
        sravn: int = 0
        perest: int = 0

        pivot: int
        l_hold: int = left
        r_hold = right
        pivot = data[left].name
        while left < right:
            sravn += 1
            while data[right].name >= pivot and left < right:
                right = right - 1
                sravn += 1
            if left != right:
                data[left].id = int(data[right].id)
                data[left].name = str(data[right].name)
                data[left].age = int(data[right].age)
                left = left + 1
                sravn += 1
                perest += 1
            while data[left].name <= pivot and left < right:
                sravn += 1
                left = left + 1
            if left != right:
                data[right].id = int(data[left].id)
                data[right].name = str(data[left].name)
                data[right].age = int(data[left].age)
                right = right - 1
                sravn += 1
                perest += 1

        data[left].name = pivot
        pivot = left
        left = l_hold
        right = r_hold
        if left < pivot:
            sravn += 1
            quicksort_name(data, left, pivot - 1)
        if right > pivot:
            sravn += 1
            quicksort_name(data, pivot + 1, right)

        return [sravn, perest]
    except Exception as e:
        print(e)
