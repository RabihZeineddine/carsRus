class Node:
    def __init__(user, num):
        user.data = num
        user.next = None


class QuickSort:
    def partitionLast(user, start, end):
        if (start == end or start == None or end == None):
            return start

        Pivot_Last = start
        curr = start
        pivot = end.data


        while (start != end):
            if (start.data < pivot):
                # keep tracks of last modified item
                Pivot_Last = curr
                temp = curr.data
                curr.data = start.data
                start.data = temp
                curr = curr.next
            start = start.next


        temp = curr.data
        curr.data = pivot
        end.data = temp

        return Pivot_Last

    def sort(user, start, end):
        if (start == None or start == end or start == end.next):
            return

        # split list and partition recurse
        Pivot_Last = user.partitionLast(start, end)
        user.sort(start, Pivot_Last)


        if (Pivot_Last != None and Pivot_Last == start):
            user.sort(Pivot_Last.next, end)

        elif (Pivot_Last != None and Pivot_Last.next != None):
            user.sort(Pivot_Last.next.next, end)
