import zipfile,sys,itertools
from timeit import default_timer as timer

charset = "0123456789abcdefghijklmnopqrstuvwxyz"
fileName = ""
password = ""
zip = zipfile.ZipFile(fileName)

def brute():
	done = False
	for i in range(2,8):
		if(done == True):
			break
		for passwd in itertools.product(charset,repeat=i):
			passwd = ''.join(passwd)
			if(extratFile(passwd)):
				print("Password : {0}".format(passwd))
				done = True
				break

def extratFile(password):
	try:
		zip.extractall(pwd=bytes(password,'utf-8'))
		return True
	except:
		return False

def main():
	fileName = input("Enter filename: ")
	start = timer()
	brute()
	totalTime = timer()-start
	print("{0}".format(totalTime))

if __name__ == "__main__":
	main()
