import pickle


dict0 = {1: "One", 2: "Two"}
list0 = ["abc", "def"]

print("Pickling..")
# Open for "wb" (write binary)
out_stream = open("test_pickle.pkl", "wb")

# Dump into filestream
pickle.dump(dict0, out_stream)
pickle.dump(list0, out_stream)

# Save file
out_stream.close()

print("Unpickling..")
# Read binary (rb)
in_stream = open("test_pickle.pkl", "rb")
dict1 = pickle.load(in_stream)
list1 = pickle.load(in_stream)
in_stream.close()
print dict1
print list1
