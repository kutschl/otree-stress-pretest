def writeBotsFile(url: str, imports: str, code: str):
    output = f"""{imports}

class PlayerBot(Bot):
    def play_round(self):
        {code}  
"""
    f = open(url, 'w')
    f.write(output)
    f.close()



