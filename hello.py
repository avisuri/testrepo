# comment
def say_hello():
	print("Good midday, world!")
	print("Bye bye world!")

def say_something(something):
	if something:
		something.reverse()
		print(" ".join(something))
	else:
		print("Hello world!")
