class Node:
    def __init__(self, num):
        self.data = num
        self.next = None


class QuickSort:

    def __init__(self):
        self.head = None

    def addNode(self, data):
        if (self.head == None):
            self.head = Node(data)
            return

        curr = self.head
        while (curr.next != None):
            curr = curr.next

        new = Node(data)
        curr.next = new

    def printList(self, n):
        while (n != None):
            print(n.data, end=" ")
            n = n.next


    def partitionLast(self, start, end):
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

    def sort(self, start, end):
        if (start == None or start == end or start == end.next):
            return

        # split list and partition recurse
        Pivot_Last = self.partitionLast(start, end)
        self.sort(start, Pivot_Last)


        if (Pivot_Last != None and Pivot_Last == start):
            self.sort(Pivot_Last.next, end)

        elif (Pivot_Last != None and Pivot_Last.next != None):
            self.sort(Pivot_Last.next.next, end)


if __name__ == "__main__":
    ll = QuickSort()
    ll.addNode(30)
    ll.addNode(3)
    ll.addNode(4)
    ll.addNode(20)
    ll.addNode(5)

    N = ll.head
    while (N.next != None):
        N = N.next

    print("\nLinked List before sorting")
    ll.printList(ll.head)

    # Function call
    ll.sort(ll.head, N)

    print("\nLinked List after sorting")
    ll.printList(ll.head)
