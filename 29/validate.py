
def validate(brackets):
  stack = []
  tokens = {
    "{": "}",
    "[": "]",
    "(": ")"
  }

  for char in brackets:
    if tokens.get(char, False):
      stack.append(char)
    if char in ["]", "}", ")"]:
      openBracket = stack.pop()
      if tokens[openBracket] != char:
        return False

  return True



print validate("{ [ ] ( ) }")
print validate("{ [ ( ] ) }")

