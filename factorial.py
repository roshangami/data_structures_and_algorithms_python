#!/usr/bin/python -tt
import sys
def main():
  try:
    num = int(sys.argv[1])
    num=num+1
  except Exception as e:
    print "Enter command line argument !"
    sys.exit(1)
  ans = 1
  for val in range(1, num):
    ans = val*ans
  print ans

if __name__ == "__main__":
  main()
