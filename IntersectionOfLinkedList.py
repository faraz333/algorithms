class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getIntersectionNode(headA, headB):
    # Helper function to calculate the length of a linked list
    def get_length(node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # Get lengths of both linked lists
    lenA = get_length(headA)
    lenB = get_length(headB)

    # Align the starting points of the two linked lists
    while lenA > lenB:
        headA = headA.next
        lenA -= 1
    while lenB > lenA:
        headB = headB.next
        lenB -= 1

    # Traverse both lists and check for intersection
    while headA and headB:
        if headA == headB:
            return headA  # Intersection found
        headA = headA.next
        headB = headB.next

    return None  # No intersection


# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


# Helper function to create an intersection between two lists
def create_intersection(list1, list2, intersection_val):
    # Create the intersection node
    intersection = ListNode(intersection_val)

    # Find the last node of list1 and list2
    tail1 = list1
    tail2 = list2

    while tail1 and tail1.next:
        tail1 = tail1.next
    while tail2 and tail2.next:
        tail2 = tail2.next

    # Connect the last nodes to the intersection node
    tail1.next = intersection
    tail2.next = intersection


# Helper function to print the linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Test Cases
def test_intersection():
    # Test Case 1: Lists intersect at some node
    listA = create_linked_list([1, 3, 5, 7])
    listB = create_linked_list([2, 4])
    create_intersection(listA, listB, 8)  # Create intersection at node 8

    result = getIntersectionNode(listA, listB)
    print(f"Test Case 1: Intersection at node with value {result.val if result else None}")

    # Test Case 2: No intersection
    listA = create_linked_list([1, 2, 3])
    listB = create_linked_list([4, 5, 6])

    result = getIntersectionNode(listA, listB)
    print(f"Test Case 2: Intersection at node {result}")

    # Test Case 3: Intersection at the head
    listA = create_linked_list([1, 2, 3])
    listB = listA  # Both lists are the same, so intersection is at the head

    result = getIntersectionNode(listA, listB)
    print(f"Test Case 3: Intersection at node with value {result.val if result else None}")

    # Test Case 4: One list is empty
    listA = create_linked_list([1, 2, 3])
    listB = None

    result = getIntersectionNode(listA, listB)
    print(f"Test Case 4: Intersection at node {result}")

    # Test Case 5: Intersection at the end of both lists
    listA = create_linked_list([1, 3, 5, 7, 9])
    listB = create_linked_list([2, 4, 6])
    create_intersection(listA, listB, 10)  # Create intersection at node 10

    result = getIntersectionNode(listA, listB)
    print(f"Test Case 5: Intersection at node with value {result.val if result else None}")

    # Test Case 6: One list is longer than the other
    listA = create_linked_list([1, 3, 5, 7, 9, 11])
    listB = create_linked_list([2, 4])
    create_intersection(listA, listB, 8)  # Create intersection at node 8

    result = getIntersectionNode(listA, listB)
    print(f"Test Case 6: Intersection at node with value {result.val if result else None}")

    # Test Case 7: Both lists are the same
    listA = create_linked_list([1, 2, 3, 4])
    listB = listA  # Same reference, so intersection is at the head

    result = getIntersectionNode(listA, listB)
    print(f"Test Case 7: Intersection at node with value {result.val if result else None}")


test_intersection()