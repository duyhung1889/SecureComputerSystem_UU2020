import os

filename = "access_file.txt"

def test1(filename):
	f = open(filename, "w")
	mess = input("Enter input data: ")
	f.write(mess)
	f.close()

def test2(filename):
	f = open(filename, "w")
	mess = input("Enter input data: ")
	os.chmod(filename,0o004)
	f.write(mess)
	f.close()

def test3(filename):
	f = open(filename, "r")
	mess = input("Enter input data: ")
	os.remove(filename)
	f.write(mess)
	f.close()

def main():
	print("1.Test1 \n 2.Test2 \n 3.Test3")
	test = int(input("Input test to run: "))
	if test == 1:
		test1(filename)
	elif test == 2: 
		test2(filename)
	elif test == 3: 
		test3(filename)

if __name__ == '__main__':
	main()

