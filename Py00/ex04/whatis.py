from sys import argv
def whatis(number : int):
	if (number % 2 == 0):
		print("I'm Even.")
	else:
		print("I'm Odd.")

try:
	assert len(argv) > 1, ""
	assert len(argv) <= 2, "AssertionError: more than one argument is provided"
	assert argv[1].isdigit() == True, "AssertionError: argument is not an integer"
	whatis(int(argv[1]))
except AssertionError as msg:
	if (msg.args[0]):
		print(msg)