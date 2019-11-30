def no_teen_sum(a, b, c):
  return fix_teen(a)+fix_teen(b)+fix_teen(c)


def fix_teen(value):

  if ((value >= 13) and (value < 15)) or ((value > 16) and (value <= 19)):
    return 0
  else:
    return value
