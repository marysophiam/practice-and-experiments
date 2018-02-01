# Cracking the Coding Interview 1.1
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?


# using add'l data structures

def is_unique(my_string):

	char_dict = {}
	# try implementing with a set instead?

	for char in my_string:
		if char in char_dict:
			print "duplicate(s) found"
			return False

		char_dict[char] = True

	print "all unique"
	return True


# is_unique("python")
# is_unique("javascript")


# without add'l data structures

def is_unique_v2(my_string):

	for i, char in enumerate(my_string):
		for j, other_char in enumerate(my_string):
			if i != j and char == other_char:
				print "duplicate(s) found"
				return False

	print "all unique"
	return True


# is_unique_v2("python")
# is_unique_v2("javascript")
