
def main():
  li = [5,7,3,6,1,2,8]
  print "li:",li
  for pivot in range(len(li)):
    pivot_e=li[pivot]
    for val in range(len(li[:pivot]))[::-1]:
#      print "list:", (li[:pivot])[::-1]
#      print "pivot:",li[pivot]
#      print "val:",li[val]
#      print "condition:", str(li[pivot] < li[val])
      if pivot_e < li[val]:
        li[val+1]=li[val]
#        print "list inside:  ",li
        if val == 0:
          li[val]=pivot_e
      else:
        li[val+1]=pivot_e
        break
#    print "sorted list:",li
  print li

if __name__ == "__main__":
  main()
        
