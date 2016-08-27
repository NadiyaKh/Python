f=open("d:\\Python\\Note.doc",'r')
lines = []
for i in range(4):
	lines.append(f.readline()) # read single line

print ('lengths is {}\n'.format(len(lines)))
for line in lines:
	print (line)

f.close()



new = open("new file",w)

new.write("sdfsadfads\n")
new.write("vcbcvbxcvb\n")
new.write("\n")
....

new.flush()

verse = [
		"sdfsadfads\n",
		"vcbcvbxcvb\n"
		"\n"
		]

new.writelines(verse)
new.close()


new = open("new file",a)

verse = [
		"sdfsadfads\n",
		"vcbcvbxcvb\n"
		"\n"
		]

new.writelines(verse)
new.close()


f=open('dsfasd')
try: # тут весь код має бути
except: # виловлювання помилок
finally:
	f.close()



with open("new file") as datasource: #datasource як змінна
	print("{} lines".format(len(datasource.readlines)))