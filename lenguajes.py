
# Shunting Yard Algorithm

# Shunt() function containing the string
# argument 'infix' - regular expression
def shunt(infix):
  # Dictionary for special characters gives them an order of precedence
  # * = 0 or more
  # + = 1 or more
  # ? = 0 or 1
  # | = or
  # . = concatenate
  specials = {'*': 60, '+': 55, '?': 50, '.': 40, '|': 20}

  # Initializing empty pofix and stack strings
  pofix, stack = "", ""  # Here we push operators in or out

  # This function reads the infix regular
  # expression one character at a time
  for c in infix:
    # Determining whether the character is an opening bracket
    if c == '(':
      stack = stack + c  # if 'c' == '(', then add it to the stack
    # Determining whether the next character is a closing bracket
    elif c == ')':
      # while the end of the stack is not an opening bracket
      while stack[-1] != '(':  # [-1] denotes any character at the end of the string
        pofix = pofix + stack[-1]  # places the character at the end of the stack in the pofix expression
        # Popping the stack - Removes the second-last character
        stack = stack[:-1]  # [:-1] denotes up to or including the last character
      stack = stack[:-1]  # removes the open bracket in the stack
    # Determine whether the character is in the 'specials' dictionary
    elif c in specials:
      while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
        pofix, stack = pofix + stack[-1], stack[:-1]
      stack = stack + c

    else:
      # Appending the character read in
      # from the infix regular expression into
      # the pofix regualr expression
      pofix = pofix + c

  while stack:
    pofix, stack = pofix + stack[-1], stack[:-1]

  # returns pofix argument
  return pofix

# Examples
# print(shunt("(a.b)|(c*.d)"))
# print(shunt("(a|b.c).c*"))

# Thompsons construction Algorithm

