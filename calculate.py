class Calculate:
    def __init__(self):
        self.__in_string = ""
        self.__precedance = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "^": 4,
            "(": 5,
            ")": 5,
        }

    def __extract_num(self, index):
        num = ""
        has_dec = False
        for digit in self.__in_string[index:]:
            if digit.isdigit():
                num += digit
            elif digit == "." and not has_dec:
                num += digit
                has_dec = True
            else:
                break
        return num

    def update(self, in_string):
        self.__in_string = in_string.strip()

    def __tokenize(self):
        i = 0
        tokens = []
        while i < len(self.__in_string):
            if self.__in_string[i].isdigit() or self.__in_string[i] == ".":
                num = self.__extract_num(i)
                i += len(num) - 1
                tokens.append(float(num))
            elif self.__in_string[i] in self.__precedance:
                tokens.append(self.__in_string[i])
            i += 1
        return tokens

    def __parse(self, tokens):
        postfix = []
        op_stack = []
        for token in tokens:
            if isinstance(token, float):
                postfix.append(token)
            elif token in self.__precedance:
                if token == "(":
                    op_stack.append(token)
                elif token == ")":
                    while len(op_stack) != 0 and op_stack[-1] != "(":
                        postfix += op_stack.pop()
                    if len(op_stack) == 0 and op_stack[-1] != "(":
                        raise SyntaxError("Mismatched Parenthises (not enough)")
                    op_stack.pop()
                else:
                    while (
                        len(op_stack) != 0
                        and op_stack[-1] != "("
                        and (
                            self.__precedance[op_stack[-1]] > self.__precedance[token]
                            or (
                                self.__precedance[op_stack[-1]]
                                == self.__precedance[token]
                                and token != "^"
                            )
                        )
                    ):
                        postfix.append(op_stack.pop())
                    op_stack.append(token)

        for op in reversed(op_stack):
            if op == "(":
                raise SyntaxError("Mismatched Parenthises (too many)")
            postfix.append(op)
        return postfix

    def __eval_postfix(self, postfix):
        eval_stack = []
        for token in postfix:
            if isinstance(token, float):
                eval_stack.append(token)
            else:
                val2 = eval_stack.pop()
                val1 = eval_stack.pop()
                result = 0
                match token:
                    case "+":
                        result = val1 + val2
                    case "-":
                        result = val1 - val2
                    case "*":
                        result = val1 * val2
                    case "/":
                        result = val1 / val2
                    case "^":
                        result = val1**val2
                eval_stack.append(result)
        return eval_stack.pop()

    def solve(self):
        tokens = self.__tokenize()
        if len(tokens) == 0:
            raise SyntaxError("Empty expression")
        postfix = []
        try:
            postfix = self.__parse(tokens)
        except Exception as e:
            print(e)
            raise SyntaxError("Parse error")

        try:
            return self.__eval_postfix(postfix)
        except Exception as e:
            print(e)
            raise ArithmeticError("Evaluation of postfix failed")
