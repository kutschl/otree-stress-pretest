import numpy as np

# Generator
output = ""
for i in np.arange(1, 21, 1):
    output = output + "\n \n"
    comment = "# Decision " + str(i)
    output = output + comment + "\n"

    for j in np.arange(1, 22, 1):
        output = output + "D" + str(i) + "_" + str(j) + " = IntegerField('D" + str(i) + "', " + str(j) + ") \n"

# Output
print(output)
