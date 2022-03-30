import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd


def addQuotationMarks(string):
    # This function makes sure a string is framed by quotation marks
    if string[0] != '"':
        string = '"' + string + '"'
    return string


def escapeUmlaute(string):
    # This function escapes ä,ö,ü,ß to it's HTML-equivalent
    return string.replace("ä", "&auml;").replace("ö", "&ouml;").replace("ü", "&uuml;").replace("ß", "&szlig;").replace(
        "Ö", "&Ouml;")


# Read in meal names (in lottery case, this would be e.g. the lottery amounts to put on LHS, RHS)
menu = pd.read_excel("meal_list_April.xlsx")
menu = menu.set_index('num')

##################################################################################################
# PART 1:
# The following are HTML bits which do not vary between the different screens
# I simplified it now, but I had many bits and pieces because for every bit I have the option between:
# A) using """ """ as brackets --> then I can integrate { which oTree needs e.g. for {% next_button %}
# B) integrating a local variable with f""" which then varies within the loop (see the next section)
# Since I didnt figure out how to bracket such that both of this is possible,
# I use different approaches for different bits of code and paste them all together in Part 3
##################################################################################################


html_start1 = """
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!DOCTYPE html>
    <html>
    <head>
    <meta  charset="utf-8" name="viewport" content="width=device-width, initial-scale=1">
    <style>
    </style>
    </head>
    <body>
<p>&nbsp;</p>
"""

##################################################################################################
# PART 2:
# Now, in a loop, I generate all the inputs requiring local input.
# In this case, it is the name of the meal, which varies across HTML files.
##################################################################################################

for i in range(1, 29):
    meal = str(menu.loc[i, "Gericht_name"])
    if i < 28:
        des = f"das Gericht '{escapeUmlaute(meal)}'"
        des2 = f"dem Gericht '{escapeUmlaute(meal)}'"
    elif i == 28:
        des = "ein K&auml;sebr&ouml;tchen"
        des2 = "einem K&auml;sebr&ouml;tchen"
    html_start2b = escapeUmlaute(f"""
          <p>Sie k&ouml;nnen entweder ein K&auml;sebr&ouml;tchen oder {des} bei Ihrer Auszahlung erhalten.""")

    ##################################################################################################
    # PART 3:
    # Piece together
    ##################################################################################################

    # Piece together WTP inquiries for meals offered in the Mensa during field experiment
    # WTP without anything
    html_control = html_start1 + html_start2b
    Html_file = open(f"output_by_gen_html_example/food_1_{i}.html", "w")
    Html_file.write(html_control)
    Html_file.close()
    # Emissions guess
