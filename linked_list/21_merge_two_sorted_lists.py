class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
#     stop = tmp = ListNode()
#     while list1 and list2:
#         if list1.val < list2.val:
#             tmp.next = list1
#             list1 = list1.next
#         else:
#             tmp.next = list2
#             list2 = list2.next
#         tmp = tmp.next
#
#     if list1:
#         tmp.next = list1
#     if list2:
#         tmp.next = list2
#
#     return stop.next


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    if (list1 is None) or (list2 and list1.val > list2.val):
        list1, list2 = list2, list1
    if list1:
        list1.next = merge_two_lists(list1.next, list2)
    return list1


head_node = ListNode(1)
node_1 = ListNode(2)
tail_node = ListNode(4)

head_node.next = node_1
node_1.next = tail_node

head_node2 = ListNode(1)
node_2 = ListNode(3)
tail_node2 = ListNode(4)

head_node2.next = node_2
node_2.next = tail_node2

iterator = merge_two_lists(head_node, head_node2)
while iterator:
    print(iterator.val)
    iterator = iterator.next
