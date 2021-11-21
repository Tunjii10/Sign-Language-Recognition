#label_map is a list of various labels
label_map = ["I", "My", "You", "Father", "Mother", "How", "Name", "Smile", "Hello", "Morning", "Night", "Afternoon" ]

i = 1

path = r"Tensorflow\workspace\training_demo\annotations"
with open(path + "\label_map.pbtxt", "w") as f:
	for label in label_map:
		f.write("item { \n")
		f.write("\tid : {} \n". format(i))
		f.write("\tname : \"{}\"\n". format(label))
		f.write('}\n\n')
		i += 1
		