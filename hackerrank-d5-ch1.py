class SinglyLinkedListNode(object):
    """[summary]

    Args:
        object ([type]): [description]
    """

    def __init__(self, node_data):
        """[summary]

        Args:
            node_data ([type]): [description]
        """
        self.data = node_data
        self.next = None


class SinglyLinkedList(object):
    """[summary]

    Args:
        object ([type]): [description]
    """

    def __init__(self):
        """[summary]"""
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        """[summary]

        Args:
            node_data ([type]): [description]
        """
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def mergeLists(
    head1: SinglyLinkedListNode, head2: SinglyLinkedListNode
) -> SinglyLinkedListNode:
    """[summary]

    Args:
        head1 (SinglyLinkedListNode): [description]
        head2 (SinglyLinkedListNode): [description]

    Returns:
        SinglyLinkedListNode: [description]
    """
    rst = SinglyLinkedListNode(None)
    temp_ls = rst

    while head1 and head2:
        if head1.data <= head2.data:
            temp_ls.next = head1
            head1 = head1.next
        else:
            temp_ls.next = head2
            head2 = head2.next
        temp_ls = temp_ls.next

    if head1 is None:
        temp_ls.next = head2

    if head2 is None:
        temp_ls.next = head1

    return rst.next


if __name__ == "__main__":
    mergeLists()
