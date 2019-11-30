def sum13(nums):
  num13s=0
  value_sum=0
  skip=False
  for i in nums:
    if skip and (i != 13):
      skip=False
    else:
      if (i != 13) and (not skip):
        value_sum=value_sum+i
      else:
        num13s=num13s+1
        skip=True

  if (len(nums) == 0):
    return 0

  return value_sum