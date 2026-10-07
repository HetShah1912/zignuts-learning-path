# Figure out a way to store 9 and 9.0 as seperate value in sets (can use built in data types)

values = {9, 9.0, 8, 8.0, 5, 5.0}
print(values)
seperatedValues = {"9", 9.0, "8", 8.0, "5", "5.0"}
print(seperatedValues)

tupleSetOfValues = {("int", 9), ("float", 9.0)} 
print(tupleSetOfValues)