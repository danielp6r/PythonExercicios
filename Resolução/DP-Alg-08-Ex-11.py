def codif(s):
  comp = []
  count = 1
  char = s[0]
  for i in range(1,len(s)):
    if s[i] == char:
      count = count + 1
    else :
      comp.append([char,count])
      char = s[i]
      count = 1
  comp.append([char,count])
  return comp
  
#main
x = ["A","A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B","A", "A", "A", "A", "A", "A", "B"]
print(codif(x))