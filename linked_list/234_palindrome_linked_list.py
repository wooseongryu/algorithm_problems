from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# def is_palindrome(head: ListNode) -> bool:
#     tmp = deque()
#
#     iterator = head
#
#     while iterator:
#         tmp.append(iterator.val)
#         iterator = iterator.next
#
#     while len(tmp) > 1:
#         if tmp.pop() != tmp.popleft():
#             return False
#     return True


def is_palindrome(head: ListNode) -> bool:
    rev = None
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev


head_node = ListNode(1)
node_1 = ListNode(2)
node_2 = ListNode(2)
tail_node = ListNode(1)

head_node.next = node_1
node_1.next = node_2
node_2.next = tail_node

print(is_palindrome(head_node))
