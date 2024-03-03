class Medium:
    def decode(self, s: str) -> str:
        stack = []

        for c in s:
            # push to stack till ]
            if c != "]":
                stack.append(c)
            else:
                # we got ] --> let's push the last substring
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr
                # pop [
                stack.pop()

                # get k --> frequency
                k = ""
                while stack and stack[-1].isdigit() and stack[-1] != "[":
                    k = stack.pop() + k
                stack.append(substr * int(k))
        return "".join(stack)
