class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    node, prev = head, None

    while node is not None:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev


head_node = ListNode(1)
node_1 = ListNode(2)
node_2 = ListNode(3)
node_3 = ListNode(4)
tail_node = ListNode(5)

head_node.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = tail_node


iterator = reverse_list(head_node)
while iterator:
    print(iterator.val)
    iterator = iterator.next
