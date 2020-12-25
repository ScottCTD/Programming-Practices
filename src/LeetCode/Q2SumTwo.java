package LeetCode;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Q2SumTwo {

    public static void main(String[] args) {
        ListNode l1 = new ListNode(2, new ListNode(4, new ListNode(3)));
        ListNode l2 = new ListNode(5, new ListNode(6, new ListNode(4)));

        ListNode result = addTwoNumbers02(l1, l2);

        List<Integer> list = new ArrayList<>();

        iterate(result, list);

        System.out.println(list);
    }

    // Not original
    // Very efficient -> 2ms
    private static ListNode addTwoNumbers02(ListNode l1, ListNode l2) {
        // Head: The start of the linked list
        // Tail: The dynamic rear part of the linked list
        ListNode head = null, tail = null;

        // The carry number
        int carry = 0;

        while (l1 != null || l2 != null) {

            // v1, v2, and sum
            int v1 = l1 == null ? 0 : l1.val, v2 = l2 == null ? 0 : l2.val, sum = v1 + v2 + carry;

            // if haed == null, the first loop -> initialize the head and tail
            // Since now the size of the linked list is 1, the head and tail should be equal
            if (head == null) {
                // sum % 10 signify the single digit
                head = tail = new ListNode(sum % 10);
                // else: second or further loop, should move the tail further
            } else {
                tail.next = new ListNode(sum % 10);
                tail = tail.next;
            }

            // sum / 10 signify the tens digit if possible (if not zero)
            // This number will be carried to the next node, which is good
            carry = sum / 10;

            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }
        // The carry may not be zero after all finished, so add a new node with carry as the last node if not zero.
        if (carry > 0) tail.next = new ListNode(carry);
        // Head is the first element in the linked list
        return head;
    }

    /**
     * Original
     * Not very efficient.
     * Convert the linked list to BigInteger and then convert back
     * Not very good.
     * But I cannot find another method, oh my world....
     */
    public static ListNode addTwoNumbers01(ListNode l1, ListNode l2) {

        List<Integer> list01 = new ArrayList<>() {
            @Override
            public String toString() {
                StringBuilder builder = new StringBuilder();
                for (int i : this) {
                    builder.append(i);
                }
                return builder.toString();
            }
        };

        List<Integer> list02 = new ArrayList<>() {
            @Override
            public String toString() {
                StringBuilder builder = new StringBuilder();
                for (int i : this) {
                    builder.append(i);
                }
                return builder.toString();
            }
        };

        iterate(l1, list01);
        iterate(l2, list02);

        Collections.reverse(list01);
        Collections.reverse(list02);

        BigInteger num01 = new BigInteger(list01.toString());
        BigInteger num02 = new BigInteger(list02.toString());

        BigInteger temp = num01.add(num02);

        String result = temp.toString();

        char[] resultArray = reverse(result.toCharArray());

        ListNode[] nodes = new ListNode[resultArray.length];
        for (int i = 0; i < resultArray.length; i++) {
            ListNode node = new ListNode(Integer.parseInt(new String(resultArray, i, 1)));
            nodes[i] = node;
        }

        for (int i = 0; i < nodes.length - 1; i++) {
            nodes[i].next = nodes[i + 1];
        }

        return nodes[0];
    }

    private static void iterate(ListNode list, List<Integer> storage) {
        storage.add(list.val);
        if (list.next == null) return;
        iterate(list.next, storage);
    }

    private static char[] reverse(char[] target) {
        char[] result = new char[target.length];
        int index = 0;
        for (int i = target.length - 1; i >= 0; i--) {
            result[index] = target[i];
            index++;
        }
        return result;
    }

    // Given
    public static class ListNode {

        int val;
        ListNode next;

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

}
