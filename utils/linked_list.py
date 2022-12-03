from typing import Any, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        head = self
        res = ""
        while head:
            res += str(head.val)

            if head.next:
                res += " -> "
            head = head.next
        return res


def linked_list(vals: list[Any]) -> Optional[ListNode]:
    cur = ListNode()
    sentinel = cur

    for val in vals:
        cur.next = ListNode(val)
        cur = cur.next

    return sentinel.next


def main():
    arr = [1, 2, 3, 4]
    head = linked_list(arr)
    print(head)


if __name__ == "__main__":
    main()
