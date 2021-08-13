# Given a string formula representing a chemical formula, return the count of each atom.
# The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
# One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.

# For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
# Two formulas are concatenated together to produce another formula.

# For example, "H2O2He3Mg4" is also a formula.
# A formula placed in parentheses, and a count (optionally added) is also a formula.

# For example, "(H2O2)" and "(H2O2)3" are formulas.
# Return the count of all elements as a string in the following form: the first name (in sorted order),
# followed by its count (if that count is more than 1), followed by the second name (in sorted order), 
# followed by its count (if that count is more than 1), and so on.

class Solution:

    # Original
    # 100%
    # Split the formula according to parathethesis()
    # Stack + Map
    def countOfAtoms2(self, formula: str) -> str:
        length = len(formula)
        stack = []
        stack.append({})
        i = 0
        while i < length:
            c = formula[i]
            if c == '(':
                # Push a new item into stack
                stack.append({})
                i += 1
            elif c == ')':
                # Find factor number
                number = 1
                temp = ''
                i += 1
                while i < length and formula[i].isdigit():
                    temp += formula[i]
                    i += 1
                if len(temp) != 0:
                    number = int(temp)
                # Pop stack (Merge current stack item into last stack item)
                item = stack.pop()
                for name in item:
                    if name not in stack[-1]:
                        stack[-1][name] = 0
                    stack[-1][name] += item[name] * number
            else:
                # Firstly parse the atom name
                name = c
                i += 1
                while i < length and formula[i].islower():
                    name += formula[i]
                    i += 1
                # Then parse the number after atom name
                number = 1
                temp = ''
                while i < length and formula[i].isdigit():
                    temp += formula[i]
                    i += 1
                if len(temp) != 0:
                    number = int(temp)
                # Put other charaters into the current stack item
                if name not in stack[-1]:
                    stack[-1][name] = 0
                stack[-1][name] += number

        result = ''
        for key in sorted(stack[0].keys()):
            result += key
            val = stack[0][key]
            if val > 1:
                result += str(val)
        return result

    # Original
    # Failed attemp
    def countOfAtoms(self, formula: str) -> str:
        def func(sub_formula: str):
            m = {}
            name = ''
            number = ''
            index = -1
            for i in range(len(sub_formula)):
                if i < index:
                    continue
                c = sub_formula[i]
                if c.isupper():
                    if len(number) != 0:
                        m[name] += int(number)
                        number = ''
                        name = ''
                    if len(name) == 0:
                        name += c
                    else:
                        if name not in m:
                            m[name] = 0
                        m[name] += 1
                        name = c
                elif c.islower():
                    name += c
                elif c.isdigit():
                    if name not in m:
                        m[name] = 0
                    number += c
                elif c == '(':
                    # This is wrong
                    # Incompatible case: (  ()  ()  )
                    index = sub_formula.rfind(')')
                    sub_m = func(sub_formula[i + 1: index])
                    factor = 1
                    if index != len(sub_formula) - 1:
                        temp = ''
                        while index < len(sub_formula) - 1 and sub_formula[index + 1].isdigit():
                            temp += sub_formula[index + 1]
                            index += 1
                        factor = int(temp)
                    if factor > 1:
                        index += 1
                    for k in sub_m:
                        if k not in m:
                            m[k] = 0
                        m[k] += sub_m[k] * factor
            if len(name) != 0:
                if name not in m:
                    m[name] = 0
                if len(number) != 0:
                    m[name] += int(number)
                else:
                    m[name] += 1
            return m
        mp = func(formula)
        result = ''
        for key in sorted(mp.keys()):
            result += key
            val = mp[key]
            if val > 1:
                result += str(val)
        return result


if __name__ == '__main__':
    print(Solution().countOfAtoms2('H2O') == 'H2O')
    print(Solution().countOfAtoms2('Mg(OH)2') == 'H2MgO2')
    print(Solution().countOfAtoms2('K4(ON(SO3)2)2') == 'K4N2O14S4')
    print(Solution().countOfAtoms2('Be32') == 'Be32')
    print(Solution().countOfAtoms2('(((Be32)))') == 'Be32')
    print(Solution().countOfAtoms2('H11He49NO35B7N46Li20') == 'B7H11He49Li20N47O35')
    print(Solution().countOfAtoms2('HOH2') == 'H3O')
    print(Solution().countOfAtoms2('((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14') == "B18900Be18984C4200H5446He1386Li33894N50106O22638")
