def NULL_not_found(object: any) -> int:
	if ((not object) or object != object):
		if (object is None):
			print("Nothing:", end=' ')
		elif (isinstance(object, bool)):
			print("Fake:", end=' ')
		elif (isinstance(object, int)):
			print("Zero:", end=' ')
		elif (isinstance(object, str)):
			print("Empty:", end=' ')
		elif (isinstance(object, float)):
			print("Cheese:", end=' ')
		print(object, type(object))
		return 0
	else:
		print("Type not Found")
		return 1
