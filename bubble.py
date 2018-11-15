import sys

def swap(li, first, second):
  temp = li[first]
  li[first]=li[second]
  li[second]=temp

def main():
  li = [5,3,9,1,7,2]
  print li
  for val in range(len(li)):
    for num in li[:-1]:
      print num
      if num > li[li.index(num)+1]:
#        swap(li, li.index(num), li.index(num)+1)
        a=li.index(num)
        b=li.index(num)+1
#        li[li.index(num)],li[li.index(num)+1] = li[li.index(num)+1],li[li.index(num)]
        li[a]=li[b]
        li[b]=num
    print li 
  print li

if __name__ == '__main__':
  main()
