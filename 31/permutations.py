# this needs some love... it is wrong

def perms(string, output=[]):
  if len(string) < 1:
    return output

  first = string[0]
  rest = string[1:]
  output.append(first)
  for i in range(0, len(rest)):
    perm = rest[:i] + first + rest[i:]
    output.append(perm)

  return perms(rest, output)


print perms('Dianna')
