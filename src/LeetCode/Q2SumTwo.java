package LeetCode;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Not very effective.
 */
public class Q2SumTwo {

    public static void main(String[] args) {
        /*ListNode l1 = new ListNode(2, new ListNode(4, new ListNode(3)));
        ListNode l2 = new ListNode(5, new ListNode(6, new ListNode(4)));*/

        ListNode l1 = new ListNode(9);
        ListNode l2 = new ListNode(1, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9,
                new ListNode(9, new ListNode(9, new ListNode(9, new ListNode(9))))))))));

        ListNode result = addTwoNumbers(l1, l2);

        List<Integer> list = new ArrayList<>();

        iterate(result, list);

        System.out.println(list);
    }

    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {

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
