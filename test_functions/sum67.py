def sum67(nums):
  skip67s=False
  sum_of_values=0
  for i in nums:
    if skip67s:
      if i == 7:
        skip67s=False
    else:
      if i == 6:
        skip67s=True
      else:
        sum_of_values=sum_of_values+i
        
  return sum_of_values