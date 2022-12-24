import os
import sys
import inspect


def _prompt(func_name):
    # awfully hacky, but pretty flexible for prompt lol
    import re, readline
    i = readline.get_current_history_length()
    line = ''
    code = []

    while not re.match(r".*{}\s*\(".format(func_name), line):
        line = readline.get_history_item(i)
        relevant = line.lstrip("\\\n")

        # tbh at this point just exploring how many edge parsing cases
        # i could possibly catch without a tokenizer
        if relevant:
            if relevant == func_name and code[-1] == '(':
                return ''.join(code[:-1:-1])

            code.append(relevant)
        i -= 1
    return ''.join(code[::-1])


def _in_ipython():
    try:
        return __IPYTHON__
    except NameError:
        return False


def _parens(code):
    """Get index of closing paren"""
    opening = closing = 0
    marks = []

    for i, v in enumerate(code):

        if code[i-1] != "\\" or code[i-2:i] == "\\\\":

            if v in ("'", '"'):
                marks.append(v)

            elif marks and marks[-1] == v:
                marks.pop()

                if not marks:
                    return i

        if len(marks) != 1:
            if   v == '(': opening += 1
            elif v == ')': closing += 1

        if closing > opening:
            return i


def arg_repr():
    func_name = sys._getframe(1).f_code.co_name
    in_ipython = _in_ipython()
    in_interactive_shell = hasattr(sys, "ps1")

    if in_interactive_shell and not in_ipython:
        code = _prompt(func_name)

    else: # in ipython/ file
        upper_frame = sys._getframe(2)
        #        line called              first line in frame that called
        lineo = upper_frame.f_lineno - upper_frame.f_code.co_firstlineno
        code = inspect.getsource(upper_frame)

        # seek beginning of call line by traversing the code until the lineo-th newline
        line = p = 0
        while line != lineo:
            if code[p] == os.linesep:
                line += 1
            p += 1

        # slice the code
        # from beginning of call (after opening paren)
        # up until the last relevant closing paren
        code = code[p:]

    code = code[code.index(func_name) + len(func_name):]
    code = code[code.index('(') + 1:]
    code = code[:_parens(code)] # _parens might return None but that's ok, [:None] is valid

    # code is now a repr of the function call arguments
    return code
