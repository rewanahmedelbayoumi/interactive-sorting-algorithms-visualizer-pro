# ================= algorithms.py =================

def bubble_sort(arr):

    comps = swaps = 0
    n = len(arr)

    for i in range(n):

        for j in range(n - i - 1):

            comps += 1

            yield arr, j, j + 1, "compare", comps, swaps

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swaps += 1

                yield arr, j, j + 1, "swap", comps, swaps

    yield arr, -1, -1, "done", comps, swaps


# ======================================================

def quick_sort(arr, low=0, high=None, comps=0, swaps=0):

    if high is None:
        high = len(arr) - 1

    if low < high:

        pivot = arr[high]

        i = low - 1

        for j in range(low, high):

            comps += 1

            yield arr, j, high, "compare", comps, swaps

            if arr[j] < pivot:

                i += 1

                arr[i], arr[j] = arr[j], arr[i]

                swaps += 1

                yield arr, i, j, "swap", comps, swaps

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        swaps += 1

        yield arr, i + 1, high, "swap", comps, swaps

        pi = i + 1

        yield from quick_sort(arr, low, pi - 1, comps, swaps)

        yield from quick_sort(arr, pi + 1, high, comps, swaps)

    yield arr, -1, -1, "done", comps, swaps


# ======================================================

def selection_sort(arr):

    comps = swaps = 0
    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            comps += 1

            yield arr, min_index, j, "compare", comps, swaps

            if arr[j] < arr[min_index]:

                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

        swaps += 1

        yield arr, i, min_index, "swap", comps, swaps

    yield arr, -1, -1, "done", comps, swaps


# ======================================================

def insertion_sort(arr):

    comps = swaps = 0

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:

            comps += 1

            yield arr, j, j + 1, "compare", comps, swaps

            arr[j + 1] = arr[j]

            swaps += 1

            yield arr, j, j + 1, "swap", comps, swaps

            j -= 1

        arr[j + 1] = key

    yield arr, -1, -1, "done", comps, swaps


# ======================================================
# ================= MERGE SORT =========================
# ======================================================

def merge_sort(arr):

    comps = 0
    swaps = 0

    yield from merge_recursive(
        arr,
        0,
        len(arr) - 1,
        comps,
        swaps
    )

    yield arr, -1, -1, "done", comps, swaps


def merge_recursive(arr, left, right, comps, swaps):

    if left < right:

        mid = (left + right) // 2

        yield from merge_recursive(
            arr,
            left,
            mid,
            comps,
            swaps
        )

        yield from merge_recursive(
            arr,
            mid + 1,
            right,
            comps,
            swaps
        )

        i = left
        j = mid + 1

        temp = []

        while i <= mid and j <= right:

            comps += 1

            yield arr, i, j, "compare", comps, swaps

            if arr[i] <= arr[j]:

                temp.append(arr[i])

                i += 1

            else:

                temp.append(arr[j])

                j += 1

                swaps += 1

        while i <= mid:

            temp.append(arr[i])
            i += 1

        while j <= right:

            temp.append(arr[j])
            j += 1

        for k in range(len(temp)):

            arr[left + k] = temp[k]

            yield arr, left + k, -1, "swap", comps, swaps