def isBalanced(s: str) -> str:
    """[summary]

    Args:
        s (str): [description]ºº

    Returns:
        str: [description]
    """
    stack = []
    open_brackets = "{[("

    if len(s) % 2 != 0:
        return "NO"

    for item in s:
        if item in open_brackets:
            stack.append(item)
        elif len(stack) > 0:
            if (
                (item == "}" and stack[len(stack) - 1] == "{")
                or (item == "]" and stack[len(stack) - 1] == "[")
                or (item == ")" and stack[len(stack) - 1] == "(")
            ):
                stack.pop()
        else:
            return "NO"

    
    return "NO" if len(stack) > 0 else "YES"
  


if __name__ == "__main__":
    print(isBalanced("{[()]}"))
    print(isBalanced("{[(])}"))
    print(isBalanced("{{[[(())]]}}"))
