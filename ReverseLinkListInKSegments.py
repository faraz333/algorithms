class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseLinkedListSingleSegment(head: ListNode, K) -> (ListNode, ListNode): #head and tail


   if head is None:
        return None


   prev=None
   current=head
   tail=head# This will be our new tail of this segment
   counter=0
   while(current and counter < K): #iterate untill we have current

       temp=current.next #save next address
       current.next=prev
       prev=current
       current=temp
       counter=counter+1

   return (prev, tail) # if current is None it means we have prev as head of link list


def reverseLinkedListInSegments(head: ListNode, k: int) -> ListNode:


    if head is None:
        return None

    current=head
    prevTail=None

    while current: #current will point to next segment of list

        segHead,tail= reverseLinkedListSingleSegment(current, k)
        if  prevTail == None: #it means it is our first segment  and new head is our head
            head=segHead
            prevTail=tail #this is now our trail
        else:
            prevTail.next=segHead #our previous tail will point to out segment head
            prevTail=tail #prev tail will now point to tail of current segment
        current=tail #this is our current pointer

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
def test_reverse_linked_list_in_segments():
    # Test Case 1: Reversing in segments of size 3
    l1 = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
    result1 = reverseLinkedListInSegments(l1, 3)
    print("Reversed List in Segments of 3:")
    print_linked_list(result1)

    # Test Case 2: Reversing in segments of size 2
    l2 = create_linked_list([1, 2, 3, 4, 5, 6])
    result2 = reverseLinkedListInSegments(l2, 2)
    print("Reversed List in Segments of 2:")
    print_linked_list(result2)

    # Test Case 3: k is greater than the length of the list
    l3 = create_linked_list([1, 2, 3])
    result3 = reverseLinkedListInSegments(l3, 5)
    print("Reversed List in Segments of 5 (k > length of list):")
    print_linked_list(result3)

    # Test Case 4: Reversing in segments of size 1 (no change)
    l4 = create_linked_list([1, 2, 3, 4, 5])
    result4 = reverseLinkedListInSegments(l4, 1)
    print("Reversed List in Segments of 1:")
    print_linked_list(result4)

    # Test Case 5: Empty list
    l5 = None
    result5 = reverseLinkedListInSegments(l5, 3)
    print("Reversed Empty List:")
    print_linked_list(result5)


# Run the test cases
test_reverse_linked_list_in_segments()
