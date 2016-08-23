
#Copyright unknown 2016


from string import ascii_lowercase as az




def check(text):
	return set(text.lower()).issuperset(set(az))


print(check("abc"))

print(check('abc')==False)
print(check('absdfghjklqwertyuiopzxcvbnm') == True)
print(check('ASDFGHJKLQWERTYUIOPZXCVBNM')==True)
print(check("Quick brown fox jums over lazy dog")==True)
