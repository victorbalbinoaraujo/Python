from LinkedList import Node
from LinkedList import LinkedList

def cycle_detection(head):

    slow = head # Tortoise
    fast = head # Hare
    loop = 0

    while(slow != None and fast != None and fast.next != None):

        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            loop = 1
            break

    if loop == 1:
        slow = head

        while(slow != fast):

            slow = slow.next
            fast = fast.next

        return slow # or fast
    return None