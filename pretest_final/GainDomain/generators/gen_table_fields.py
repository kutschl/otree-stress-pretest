import numpy as np

# Input
decision_nr = 1
decisions_per_round = 21

# Generator
output = ''
tr_start = '<tr class="dtable-b3-tr">'
tr_end = '</tr>'
td =''
for i in np.arange(1, decisions_per_round+1, 1):
    td = '<td>A</td><td>{{form.D' + str(decision_nr) + '_' + str(i) + '.0}}</td><td>{{form.D' + str(decision_nr) + '_' + str(i) + '.1}}</td><td>B</td>'
    output = output + tr_start + td + tr_end + '\n'

# Output
print(output)
