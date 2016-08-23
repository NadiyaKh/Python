alphabet = "asdfghjklqwertyuiopzxcvbnm"



def check(text):
	return set(text.lower()).issuperset(set(alphabet))

print(check("abc"))