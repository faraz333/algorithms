class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def findMiddleOfLinkedList(head: ListNode) -> ListNode:
    #create a slow and fast pointer
    #move

    if head == None:
        return None

    slow=head
    fast=head

    #move slow pointer one place and fast pointers 2 places
    while(fast and fast.next): #unless we fast.next it means we can not move fast pointer
        slow = slow.next
        fast=fast.next.next #it can be None


    print("slow pointer (middle)  we have is " + str(slow.val))

    return slow


# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


# Helper function to print the linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Test cases
def test_find_middle_of_linked_list():
    # Test Case 1: Finding the middle of an odd-length linked list
    l1 = create_linked_list([1, 2, 3, 4, 5])
    middle1 = findMiddleOfLinkedList(l1)
    print("Middle of List 1:", middle1.val if middle1 else "None")

    # Test Case 2: Finding the middle of an even-length linked list
    l2 = create_linked_list([1, 2, 3, 4, 5, 6])
    middle2 = findMiddleOfLinkedList(l2)
    print("Middle of List 2:", middle2.val if middle2 else "None")

    # Test Case 3: Finding the middle of a single-element linked list
    l3 = create_linked_list([10])
    middle3 = findMiddleOfLinkedList(l3)
    print("Middle of List 3:", middle3.val if middle3 else "None")

    # Test Case 4: Finding the middle of an empty list
    l4 = None
    middle4 = findMiddleOfLinkedList(l4)
    print("Middle of List 4:", middle4.val if middle4 else "None")


# Run the test cases
test_find_middle_of_linked_list()