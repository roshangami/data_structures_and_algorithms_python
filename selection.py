
def main():
  for val in range(len(li)):
    pivot=val
    print "val->",val
    for num in li[val+1:]:
      if li[pivot] > num:
        pivot=li.index(num)
      print "list:", li[val+1:]
      print "pivot:", li[pivot]
      print "num:",num
    li[val],li[pivot] = li[pivot],li[val]

if __name__ == "__main__":
  li=[6,2,3,9,8,4,7,1,5]
  print li
  main()
  print li
