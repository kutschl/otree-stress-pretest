import numpy as np

# Input
decisions = 20
decisions_per_round = 21

# Generator
output = ""
for k in np.arange(1, decisions+1, 1):
    header = "class Tabelle" + str(k) + "(Page):"
    form_model = "form_model = ['player']"
    form_fields = "form_fields" + " = " + "["
    for i in np.arange(1, decisions_per_round, 1):
        form_fields = form_fields + "'" + "D" + str(k) + "_" + str(i) + "'" + "," + " "
    form_fields = form_fields + "'" + "D" + str(k) + "_" + str(decisions_per_round) + "'" + "]"
    output = output + header + '\n' + '\t' + form_model + '\n' + '\t' + form_fields + '\n' + '\n' + '\n'

# Output
print(output)
