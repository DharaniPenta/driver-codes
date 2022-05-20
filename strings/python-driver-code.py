# Python Driver Code

def solve(s: str) -> chr:
  # Your code goes here
  # s is the given input string
  l=s.split()
  s1=l[0]
  s2=l[1]
  li11=[int(i) for i in s1]
  li22=[int(i) for i in s2]
  li11.sort()
  li22.sort()
  list1=[str(i) for i in li11]
  list2=[str(i) for i in li22]
  c1=''.join(list1)
  c2=''.join(list2)
  if c1==c2:
    return 'recycled pair'
  else:
    return 'not recycled pair'

# The following snippet reads the input in the requir

# The following snippet reads the input in the required format. 
# Just complete the solve function above. 

T = int(input())
for i in range(T):
  test_case = input()
  answer = solve(test_case)
  print(answer)
