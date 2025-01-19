class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:

    #remove noth node from end require to mantain two pointers
    #one is current pointer which will move all the way to end
    #one is nth node pointer which will be n+1 steps behind current pointers
    #once we reach end nTh node pointer will be pointing one node behind nth node from last
    #we can use this pointer to remove nth node

    nthPRevPointer =None
    current=head
    counter=0


    while(current):
        current=current.next
        if counter==n:
            nthPRevPointer=head
        elif counter > n:
            nthPRevPointer=nthPRevPointer.next
        counter=counter+1

    #if we reached end we need to make sure that we covered atleast n steps which will translate to n-1 counter in 0 based system
    if nthPRevPointer:
        nthNode=nthPRevPointer.next
        nthPRevPointer.next = nthNode.next
    if counter == n-1: # it means we covered nth steps in 0 base system
        nthNode=head
        head=head.next
    return head


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
def test_remove_nth_from_end():
    # Test Case 1: Remove the 2nd node from the end of the list
    l1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = removeNthFromEnd(l1, 2)
    print("After removing 2nd node from the end (List 1):")
    print_linked_list(result1)

    # Test Case 2: Remove the 1st node from the end (i.e., the last node)
    l2 = create_linked_list([1, 2, 3, 4, 5])
    result2 = removeNthFromEnd(l2, 1)
    print("After removing 1st node from the end (List 2):")
    print_linked_list(result2)

    # Test Case 3: Remove the 1st node from the start (i.e., the head node)
    l3 = create_linked_list([1, 2, 3, 4, 5])
    result3 = removeNthFromEnd(l3, 5)
    print("After removing 5th node from the end (List 3):")
    print_linked_list(result3)

    # Test Case 4: Remove the only node in the list
    l4 = create_linked_list([10])
    result4 = removeNthFromEnd(l4, 1)
    print("After removing the only node (List 4):")
    print_linked_list(result4)

    # Test Case 5: Remove the 3rd node from the end (in a list with even length)
    l5 = create_linked_list([1, 2, 3, 4, 5, 6])
    result5 = removeNthFromEnd(l5, 3)
    print("After removing 3rd node from the end (List 5):")
    print_linked_list(result5)


# Run the test cases
test_remove_nth_from_end()