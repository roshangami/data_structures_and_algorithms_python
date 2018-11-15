

def swap(li,a,b):
#  print a,b
  if len(li) == 0: return
#  print "in swap->", li, "a:", a, "b:", b
  li[a], li[b] = li[b], li[a]

def main(li):
  print "Before sorting:", li
#  print "last element:", li[-1]
  pointer = 0
  for val in range(len(li)-1):
#    print "last element", li[-1]
    if li[-1] > li[val]:
      swap(li,pointer, val)
      print "pointer: ", pointer
      pointer=pointer+1
  swap(li, pointer,len(li)-1)
  print "After sorting:", li
#  if (pointer == 0) and (len(li) == 0): return 
  if (pointer == 0) and (len(li) == 0): print "returning val:",li ;return li
  else: 
    if len(li[:pointer]) != 0:
      main(li[:pointer])
    print "li left after returning:", li[:pointer]
#      return li[:pointer]
    if len(li[pointer+1:]) != 0:
      main(li[pointer+1:])
    print "li right after returning:", li[pointer+1:]
#      return li[pointer+1:]
#    li[:pointer]=main(li[:pointer])
#  if (pointer == 0) and (len(li) == 0): return
#  else: 
#    main(li[pointer+1:])
#    li[pointer+1:]=main(li[pointer+1:])
  print li
if __name__ == "__main__":
  li = [7,3,6,9,2,8,1,5]
  main(li)
  print li
