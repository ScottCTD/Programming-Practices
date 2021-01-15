package LeetCode;

/**
 * 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的
 */
public class Q21 {

    public static void main(String[] args) {
        ListNode l1 = new ListNode(1, new ListNode(2, new ListNode(4)));
        ListNode l2 = new ListNode(213, new ListNode(12312, new ListNode(8, new ListNode(921))));

        ListNode listNode = mergeTwoLists01(l1, l2);
        while (listNode != null) {
            System.out.println(listNode.val);
            listNode = listNode.next;
        }
    }

    // 01/15/2021 22:28
    // Original
    // 1ms in LeetCode, efficient.
    private static ListNode mergeTwoLists02(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        if (l2 == null) return l1;
        ListNode head = new ListNode(), tail = head;
        while (l1 != null && l2 != null) {
            if (l1.val > l2.val) {
                tail.next = l2;
                l2 = l2.next;
            } else {
                tail.next = l1;
                l1 = l1.next;
            }
            tail = tail.next;
        }
        if (l1 == null) tail.next = l2;
        if (l2 == null) tail.next = l1;
        return head.next;
    }


    // 01/15/2021 21:46
    // Original
    // 1 ms in LeetCode, not efficient comparatively.
    private static ListNode mergeTwoLists01(ListNode l1, ListNode l2) {
        if (l1 == null && l2 == null) return null;
        ListNode head = null, tail = null;
        while (l1 != null || l2 != null) {
            if (l1 == null) {
                if (head == null) {
                    head = l2;
                    break;
                }
                tail.next = l2;
                break;
            }
            if (l2 == null) {
                if (head == null) {
                    head = l1;
                    break;
                }
                tail.next = l1;
                break;
            }
            int v1 = l1.val, v2 = l2.val;
            if (head == null) {
                if (v1 > v2) {
                    head = tail = new ListNode(v2);
                    l2 = l2.next;
                } else if (v2 > v1) {
                    head = tail = new ListNode(v1);
                    l1 = l1.next;
                } else {
                    head = tail = new ListNode(v1);
                    tail.next = new ListNode(v2);
                    tail = tail.next;
                    l1 = l1.next;
                    l2 = l2.next;
                }
            } else {
                if (v1 > v2) {
                    tail.next = new ListNode(v2);
                    l2 = l2.next;
                } else if (v2 > v1) {
                    tail.next = new ListNode(v1);
                    l1 = l1.next;
                } else {
                    tail.next = new ListNode(v1);
                    tail = tail.next;
                    tail.next = new ListNode(v2);
                    l1 = l1.next;
                    l2 = l2.next;
                }
                tail = tail.next;
            }
        }
        return head;
    }

    private static class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

}
