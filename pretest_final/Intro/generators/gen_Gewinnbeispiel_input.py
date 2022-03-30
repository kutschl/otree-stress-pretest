import numpy



tr_start = """<tr class="dtable-b3-tr">"""
tr_end = """</tr>"""
td_start = """<td>"""
td_end = """</td>"""

radiobutton_checked = """<input type="radio" checked readonly style="accent-color: black;"/>"""
radiobutton_unchecked = """<input type="radio" disabled unchecked readonly style="accent-color: black;"/>"""
label_a = "A"
label_b = "B"

# Zeile 1-8: A, Zeile 9-21: B
choice_b = 8
choice_a = 21 - choice_b

output = ""
for i in numpy.arange(1, choice_b+1, 1):
    output = output + tr_start + td_start + label_a + td_end + td_start + radiobutton_unchecked + td_end + td_start + radiobutton_checked + td_end + td_start + label_b + td_end + tr_end + "\n"

for i in numpy.arange(1, choice_a, 1):
    output = output + tr_start + td_start + label_a + td_end + td_start + radiobutton_checked + td_end + td_start + radiobutton_unchecked + td_end + td_start + label_b + td_end + tr_end + "\n"

print(output)


