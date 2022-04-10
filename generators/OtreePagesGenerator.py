def writePagesFile(url: str, imports: str, pages: str, page_sequence: list):
    output = f"""{imports}

{pages}

page_sequence = {str(page_sequence).replace("'", "")}    
"""
    f = open(url, 'w')
    f.write(output)
    f.close()



def getPageWithFields(page_name: str, form_model: str, form_fields: list):
    return f"""
class {page_name}(Page):
    form_model = '{form_model}'
    form_fields = {form_fields}
    
"""


def getPageWithPass(page_name: str):
    return f"""
class {page_name}(Page):
    pass
    
"""



