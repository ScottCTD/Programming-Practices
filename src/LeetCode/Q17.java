package LeetCode;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
 * 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母
 * 回溯算法get！
 */
public class Q17 {

    public static void main(String[] args) {
        System.out.println(letterCombinations("23"));
    }

    public static List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits.isEmpty()) return result;

        char[] digitChars = digits.toCharArray();

        Map<Character, String> mapping = Map.of('2', "abc", '3', "def", '4', "ghi", '5', "jkl",
                '6', "mno", '7', "pqrs", '8', "tuv", '9', "wxyz");

        getAllCombinations(result, mapping, digitChars, 0, new StringBuilder());

        return result;
    }

    // 回溯算法 维护一个字符串temp
    // 如果它不符合条件（不等于输入的digits的长度），就执行操作
    // 操作就是将下个数字代表的映射过后的字符串的某个字符加入到这个temp
    // 穷举全部
    private static void getAllCombinations(List<String> result, Map<Character, String> mapping, char[] digitChars, int index, StringBuilder temp) {
        if (index == digitChars.length) {
            result.add(temp.toString());
        } else {
            char[] mappedString = mapping.get(digitChars[index]).toCharArray();
            for (char c : mappedString) {
                temp.append(c);
                Q17.getAllCombinations(result, mapping, digitChars, index + 1, temp);
                temp.deleteCharAt(index);
            }
        }
    }

}
