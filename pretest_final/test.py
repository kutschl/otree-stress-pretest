import random as rd





class Player:
    def xxx(self):
        rd_typ = rd.choice(['GAIN', 'LOSS'])
        rd_block = 2
        rd_table = 2
        rd_decision = 2
        # player_decision = globals()[f"{self}.B{rd_block}_{rd_typ}{rd_table}_D{rd_decision}"]
        print(2)
        print(self.__class__.__dict__[f'B{rd_block}_{rd_typ}{rd_table}_D{rd_decision}'])

    B2_GAIN2_D2 = 'GAIN'
    B2_LOSS2_D2 = 'LOSS'


p = Player()
p.xxx()


