package LeetCode;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
 * <p>
 * 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母
 * <p>
 * <p>
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

    private static void getAllCombinations(List<String> result, Map<Character, String> mapping, char[] digitChars, int index, StringBuilder temp) {
        if (index == digitChars.length) {
            result.add(temp.toString());
        } else {
            char[] mappedString = mapping.get(digitChars[index]).toCharArray();
            for (int i = 0; i < mappedString.length; i++) {
                temp.append(mappedString[i]);
                getAllCombinations(result, mapping, digitChars, index + 1, temp);
                temp.deleteCharAt(index);
            }
        }
    }

}
