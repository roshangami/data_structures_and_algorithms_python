#!/usr/bin/python -tt

def main():
  num = int(raw_input("Enter number: "))
  i=2
  flag = True
  while i != num:
   if num%i == 0:
      flag = False
      break
   i=i+1
  if flag == False:
    print "Number:",num," isn't prime"
  else:
    print "NUmber:",num," is prime"

if __name__ == "__main__":
  main()
