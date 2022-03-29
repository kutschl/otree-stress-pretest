import numpy as np

# Input
decision_nr = 1
decisions_per_round = 21

# Generator
name = "form_fields"
output = name + " = " + "["
for i in np.arange(1, decisions_per_round, 1):
    output = output + "'" + "D" + str(decision_nr) + "_" + str(i) + "'" + "," + " "
output = output + "'" + "D" + str(decision_nr) + "_" + str(decisions_per_round) + "'" + "]"

# Output
print(output)
