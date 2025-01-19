class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:

    #bounary conditions
    if l1 is None and l2 is None:
        return None

    if l1 is None and l2 is not None:
        return l2

    if l2 is None and l1 is not None:
        return l1

    head = None
    current=None
    current1=l1
    current2=l2

    while (current1 and current2): #as long as we have elements in both list we will do comparasions

        if current1.val <= current2.val:
            #do somthing
            if head == None:
                head =ListNode(current1.val)
                current=head
            else:
                current.next=ListNode(current1.val)
                current=current.next
            current1=current1.next
        else:
            #do something
            if head == None:
                head =ListNode(current2.val)
                current=head
            else:
                current.next=ListNode(current2.val)
                current = current.next
            current2 = current2.next


            #now either current1 or current2 or both are empty. we will set next node of non empty lists
    if current1:
        current.next=current1
    elif current2:
         current.next=current2

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
def test_merge_two_lists():
    # Test Case 1: Merging two non-empty sorted lists
    l1 = create_linked_list([1, 2, 4])
    l2 = create_linked_list([1, 3, 4])

    merged_list = mergeTwoLists(l1, l2)
    print("Merged List 1:")
    print_linked_list(merged_list)

    # Test Case 2: Merging one empty list and one non-empty list
    l1 = None
    l2 = create_linked_list([0])

    merged_list = mergeTwoLists(l1, l2)
    print("Merged List 2:")
    print_linked_list(merged_list)

    # Test Case 3: Merging two empty lists
    l1 = None
    l2 = None

    merged_list = mergeTwoLists(l1, l2)
    print("Merged List 3:")
    print_linked_list(merged_list)

    # Test Case 4: Merging two lists where one is much longer than the other
    l1 = create_linked_list([1, 3, 5, 7, 9])
    l2 = create_linked_list([2, 4])

    merged_list = mergeTwoLists(l1, l2)
    print("Merged List 4:")
    print_linked_list(merged_list)

    # Test Case 5: Merging two lists with duplicate values
    l1 = create_linked_list([1, 3, 5, 5])
    l2 = create_linked_list([2, 4, 5])

    merged_list = mergeTwoLists(l1, l2)
    print("Merged List 5:")
    print_linked_list(merged_list)


# Run the test cases
test_merge_two_lists()