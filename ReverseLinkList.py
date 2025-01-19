class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseLinkedList(head: ListNode) -> ListNode:

   if head is None:
        return None

   prev=None
   current=head

   while(current): #iterate untill we have current

       temp=current.next #save next address
       current.next=prev
       prev=current
       current=temp

   return prev # if current is None it means we have prev as head of link list

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
def test_reverse_linked_list():
    # Test Case 1: Reversing a non-empty linked list
    l1 = create_linked_list([1, 2, 3, 4, 5])
    reversed_l1 = reverseLinkedList(l1)
    print("Reversed List 1:")
    print_linked_list(reversed_l1)

    # Test Case 2: Reversing a single-element list
    l2 = create_linked_list([1])
    reversed_l2 = reverseLinkedList(l2)
    print("Reversed List 2:")
    print_linked_list(reversed_l2)

    # Test Case 3: Reversing an empty list
    l3 = None
    reversed_l3 = reverseLinkedList(l3)
    print("Reversed List 3:")
    print_linked_list(reversed_l3)


# Run the test cases
test_reverse_linked_list()