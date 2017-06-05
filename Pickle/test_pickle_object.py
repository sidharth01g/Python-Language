import pickle
import test_classes

emp0 = test_classes.Employee("Alice", "e101")

print emp0
print("Pickling object..")
with open("object_pickle.pkl", "wb") as pickle_out:
    pickle.dump(emp0, pickle_out)
    pickle_out.close()

print("Unpickling object..")
with open("object_pickle.pkl", "rb") as pickle_in:
    emp0_unpickled = pickle.load(pickle_in)
print emp0_unpickled
