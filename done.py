import os

def find_str(files):
	for fil in files:
		f=open(fil, "r")
		for line in f:
			for key in keywords:
				if key in line:
					print "FileName ---->", fil
					print line


def main():
	folder= os.listdir("c:\Program Files (x86)\MonitorIT\Bin")
	files=[]
	for val in folder:
		if val.startswith("MonitorITAgent") and val.endswith(".log"):
			files.append(val)
	find_str(files)

if __name__ == "__main__":
	keywords=["fail", "failed", "failure", "exception", "dump", "error", "crash"]
	main()	
