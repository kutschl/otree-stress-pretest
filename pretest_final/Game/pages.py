from ._builtin import Page, WaitPage
import random as rd


class Block1Intro(Page):
    def vars_for_template(self):
        self.player.participant.vars['block1'] = self.player.getBlock(1)
        
        self.player.participant.vars['payoff_random_block'] = rd.randint(1, 2)
        self.player.participant.vars['payoff_random_table'] = rd.randint(1, 40)
        self.player.participant.vars['payoff_random_decision'] = rd.randint(1, 21)


class Block1Table1(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE1_LOTTERY',
        'BLOCK1_TABLE1_TYPE',
        'BLOCK1_TABLE1_ORDER',
        'BLOCK1_TABLE1_SP_OPTION',
        'BLOCK1_TABLE1_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=1,
            TYPE=self.player.participant.vars['block1'][0]['TYPE'],
            ORDER=self.player.participant.vars['block1'][0]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE1_LOTTERY = self.player.participant.vars['block1'][0]['NUMBER']
        self.player.BLOCK1_TABLE1_TYPE = self.player.participant.vars['block1'][0]['TYPE']
        self.player.BLOCK1_TABLE1_ORDER = self.player.participant.vars['block1'][0]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 1: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE1_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE1_SP_DECISION



class Block1Table2(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE2_LOTTERY',
        'BLOCK1_TABLE2_TYPE',
        'BLOCK1_TABLE2_ORDER',
        'BLOCK1_TABLE2_SP_OPTION',
        'BLOCK1_TABLE2_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=2,
            TYPE=self.player.participant.vars['block1'][1]['TYPE'],
            ORDER=self.player.participant.vars['block1'][1]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE2_LOTTERY = self.player.participant.vars['block1'][1]['NUMBER']
        self.player.BLOCK1_TABLE2_TYPE = self.player.participant.vars['block1'][1]['TYPE']
        self.player.BLOCK1_TABLE2_ORDER = self.player.participant.vars['block1'][1]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 2: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE2_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE2_SP_DECISION



class Block1Table3(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE3_LOTTERY',
        'BLOCK1_TABLE3_TYPE',
        'BLOCK1_TABLE3_ORDER',
        'BLOCK1_TABLE3_SP_OPTION',
        'BLOCK1_TABLE3_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=3,
            TYPE=self.player.participant.vars['block1'][2]['TYPE'],
            ORDER=self.player.participant.vars['block1'][2]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE3_LOTTERY = self.player.participant.vars['block1'][2]['NUMBER']
        self.player.BLOCK1_TABLE3_TYPE = self.player.participant.vars['block1'][2]['TYPE']
        self.player.BLOCK1_TABLE3_ORDER = self.player.participant.vars['block1'][2]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 3: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE3_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE3_SP_DECISION



class Block1Table4(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE4_LOTTERY',
        'BLOCK1_TABLE4_TYPE',
        'BLOCK1_TABLE4_ORDER',
        'BLOCK1_TABLE4_SP_OPTION',
        'BLOCK1_TABLE4_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=4,
            TYPE=self.player.participant.vars['block1'][3]['TYPE'],
            ORDER=self.player.participant.vars['block1'][3]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE4_LOTTERY = self.player.participant.vars['block1'][3]['NUMBER']
        self.player.BLOCK1_TABLE4_TYPE = self.player.participant.vars['block1'][3]['TYPE']
        self.player.BLOCK1_TABLE4_ORDER = self.player.participant.vars['block1'][3]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 4: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE4_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE4_SP_DECISION



class Block1Table5(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE5_LOTTERY',
        'BLOCK1_TABLE5_TYPE',
        'BLOCK1_TABLE5_ORDER',
        'BLOCK1_TABLE5_SP_OPTION',
        'BLOCK1_TABLE5_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=5,
            TYPE=self.player.participant.vars['block1'][4]['TYPE'],
            ORDER=self.player.participant.vars['block1'][4]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE5_LOTTERY = self.player.participant.vars['block1'][4]['NUMBER']
        self.player.BLOCK1_TABLE5_TYPE = self.player.participant.vars['block1'][4]['TYPE']
        self.player.BLOCK1_TABLE5_ORDER = self.player.participant.vars['block1'][4]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 5: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE5_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE5_SP_DECISION



class Block1Table6(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE6_LOTTERY',
        'BLOCK1_TABLE6_TYPE',
        'BLOCK1_TABLE6_ORDER',
        'BLOCK1_TABLE6_SP_OPTION',
        'BLOCK1_TABLE6_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=6,
            TYPE=self.player.participant.vars['block1'][5]['TYPE'],
            ORDER=self.player.participant.vars['block1'][5]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE6_LOTTERY = self.player.participant.vars['block1'][5]['NUMBER']
        self.player.BLOCK1_TABLE6_TYPE = self.player.participant.vars['block1'][5]['TYPE']
        self.player.BLOCK1_TABLE6_ORDER = self.player.participant.vars['block1'][5]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 6: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE6_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE6_SP_DECISION



class Block1Table7(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE7_LOTTERY',
        'BLOCK1_TABLE7_TYPE',
        'BLOCK1_TABLE7_ORDER',
        'BLOCK1_TABLE7_SP_OPTION',
        'BLOCK1_TABLE7_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=7,
            TYPE=self.player.participant.vars['block1'][6]['TYPE'],
            ORDER=self.player.participant.vars['block1'][6]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE7_LOTTERY = self.player.participant.vars['block1'][6]['NUMBER']
        self.player.BLOCK1_TABLE7_TYPE = self.player.participant.vars['block1'][6]['TYPE']
        self.player.BLOCK1_TABLE7_ORDER = self.player.participant.vars['block1'][6]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 7: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE7_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE7_SP_DECISION



class Block1Table8(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE8_LOTTERY',
        'BLOCK1_TABLE8_TYPE',
        'BLOCK1_TABLE8_ORDER',
        'BLOCK1_TABLE8_SP_OPTION',
        'BLOCK1_TABLE8_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=8,
            TYPE=self.player.participant.vars['block1'][7]['TYPE'],
            ORDER=self.player.participant.vars['block1'][7]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE8_LOTTERY = self.player.participant.vars['block1'][7]['NUMBER']
        self.player.BLOCK1_TABLE8_TYPE = self.player.participant.vars['block1'][7]['TYPE']
        self.player.BLOCK1_TABLE8_ORDER = self.player.participant.vars['block1'][7]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 8: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE8_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE8_SP_DECISION



class Block1Table9(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE9_LOTTERY',
        'BLOCK1_TABLE9_TYPE',
        'BLOCK1_TABLE9_ORDER',
        'BLOCK1_TABLE9_SP_OPTION',
        'BLOCK1_TABLE9_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=9,
            TYPE=self.player.participant.vars['block1'][8]['TYPE'],
            ORDER=self.player.participant.vars['block1'][8]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE9_LOTTERY = self.player.participant.vars['block1'][8]['NUMBER']
        self.player.BLOCK1_TABLE9_TYPE = self.player.participant.vars['block1'][8]['TYPE']
        self.player.BLOCK1_TABLE9_ORDER = self.player.participant.vars['block1'][8]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 9: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE9_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE9_SP_DECISION



class Block1Table10(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE10_LOTTERY',
        'BLOCK1_TABLE10_TYPE',
        'BLOCK1_TABLE10_ORDER',
        'BLOCK1_TABLE10_SP_OPTION',
        'BLOCK1_TABLE10_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=10,
            TYPE=self.player.participant.vars['block1'][9]['TYPE'],
            ORDER=self.player.participant.vars['block1'][9]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE10_LOTTERY = self.player.participant.vars['block1'][9]['NUMBER']
        self.player.BLOCK1_TABLE10_TYPE = self.player.participant.vars['block1'][9]['TYPE']
        self.player.BLOCK1_TABLE10_ORDER = self.player.participant.vars['block1'][9]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 10: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE10_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE10_SP_DECISION



class Block1Table11(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE11_LOTTERY',
        'BLOCK1_TABLE11_TYPE',
        'BLOCK1_TABLE11_ORDER',
        'BLOCK1_TABLE11_SP_OPTION',
        'BLOCK1_TABLE11_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=11,
            TYPE=self.player.participant.vars['block1'][10]['TYPE'],
            ORDER=self.player.participant.vars['block1'][10]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE11_LOTTERY = self.player.participant.vars['block1'][10]['NUMBER']
        self.player.BLOCK1_TABLE11_TYPE = self.player.participant.vars['block1'][10]['TYPE']
        self.player.BLOCK1_TABLE11_ORDER = self.player.participant.vars['block1'][10]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 11: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE11_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE11_SP_DECISION



class Block1Table12(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE12_LOTTERY',
        'BLOCK1_TABLE12_TYPE',
        'BLOCK1_TABLE12_ORDER',
        'BLOCK1_TABLE12_SP_OPTION',
        'BLOCK1_TABLE12_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=12,
            TYPE=self.player.participant.vars['block1'][11]['TYPE'],
            ORDER=self.player.participant.vars['block1'][11]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE12_LOTTERY = self.player.participant.vars['block1'][11]['NUMBER']
        self.player.BLOCK1_TABLE12_TYPE = self.player.participant.vars['block1'][11]['TYPE']
        self.player.BLOCK1_TABLE12_ORDER = self.player.participant.vars['block1'][11]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 12: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE12_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE12_SP_DECISION



class Block1Table13(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE13_LOTTERY',
        'BLOCK1_TABLE13_TYPE',
        'BLOCK1_TABLE13_ORDER',
        'BLOCK1_TABLE13_SP_OPTION',
        'BLOCK1_TABLE13_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=13,
            TYPE=self.player.participant.vars['block1'][12]['TYPE'],
            ORDER=self.player.participant.vars['block1'][12]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE13_LOTTERY = self.player.participant.vars['block1'][12]['NUMBER']
        self.player.BLOCK1_TABLE13_TYPE = self.player.participant.vars['block1'][12]['TYPE']
        self.player.BLOCK1_TABLE13_ORDER = self.player.participant.vars['block1'][12]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 13: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE13_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE13_SP_DECISION



class Block1Table14(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE14_LOTTERY',
        'BLOCK1_TABLE14_TYPE',
        'BLOCK1_TABLE14_ORDER',
        'BLOCK1_TABLE14_SP_OPTION',
        'BLOCK1_TABLE14_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=14,
            TYPE=self.player.participant.vars['block1'][13]['TYPE'],
            ORDER=self.player.participant.vars['block1'][13]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE14_LOTTERY = self.player.participant.vars['block1'][13]['NUMBER']
        self.player.BLOCK1_TABLE14_TYPE = self.player.participant.vars['block1'][13]['TYPE']
        self.player.BLOCK1_TABLE14_ORDER = self.player.participant.vars['block1'][13]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 14: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE14_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE14_SP_DECISION



class Block1Table15(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE15_LOTTERY',
        'BLOCK1_TABLE15_TYPE',
        'BLOCK1_TABLE15_ORDER',
        'BLOCK1_TABLE15_SP_OPTION',
        'BLOCK1_TABLE15_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=15,
            TYPE=self.player.participant.vars['block1'][14]['TYPE'],
            ORDER=self.player.participant.vars['block1'][14]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE15_LOTTERY = self.player.participant.vars['block1'][14]['NUMBER']
        self.player.BLOCK1_TABLE15_TYPE = self.player.participant.vars['block1'][14]['TYPE']
        self.player.BLOCK1_TABLE15_ORDER = self.player.participant.vars['block1'][14]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 15: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE15_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE15_SP_DECISION



class Block1Table16(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE16_LOTTERY',
        'BLOCK1_TABLE16_TYPE',
        'BLOCK1_TABLE16_ORDER',
        'BLOCK1_TABLE16_SP_OPTION',
        'BLOCK1_TABLE16_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=16,
            TYPE=self.player.participant.vars['block1'][15]['TYPE'],
            ORDER=self.player.participant.vars['block1'][15]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE16_LOTTERY = self.player.participant.vars['block1'][15]['NUMBER']
        self.player.BLOCK1_TABLE16_TYPE = self.player.participant.vars['block1'][15]['TYPE']
        self.player.BLOCK1_TABLE16_ORDER = self.player.participant.vars['block1'][15]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 16: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE16_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE16_SP_DECISION



class Block1Table17(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE17_LOTTERY',
        'BLOCK1_TABLE17_TYPE',
        'BLOCK1_TABLE17_ORDER',
        'BLOCK1_TABLE17_SP_OPTION',
        'BLOCK1_TABLE17_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=17,
            TYPE=self.player.participant.vars['block1'][16]['TYPE'],
            ORDER=self.player.participant.vars['block1'][16]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE17_LOTTERY = self.player.participant.vars['block1'][16]['NUMBER']
        self.player.BLOCK1_TABLE17_TYPE = self.player.participant.vars['block1'][16]['TYPE']
        self.player.BLOCK1_TABLE17_ORDER = self.player.participant.vars['block1'][16]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 17: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE17_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE17_SP_DECISION



class Block1Table18(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE18_LOTTERY',
        'BLOCK1_TABLE18_TYPE',
        'BLOCK1_TABLE18_ORDER',
        'BLOCK1_TABLE18_SP_OPTION',
        'BLOCK1_TABLE18_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=18,
            TYPE=self.player.participant.vars['block1'][17]['TYPE'],
            ORDER=self.player.participant.vars['block1'][17]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE18_LOTTERY = self.player.participant.vars['block1'][17]['NUMBER']
        self.player.BLOCK1_TABLE18_TYPE = self.player.participant.vars['block1'][17]['TYPE']
        self.player.BLOCK1_TABLE18_ORDER = self.player.participant.vars['block1'][17]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 18: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE18_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE18_SP_DECISION



class Block1Table19(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE19_LOTTERY',
        'BLOCK1_TABLE19_TYPE',
        'BLOCK1_TABLE19_ORDER',
        'BLOCK1_TABLE19_SP_OPTION',
        'BLOCK1_TABLE19_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=19,
            TYPE=self.player.participant.vars['block1'][18]['TYPE'],
            ORDER=self.player.participant.vars['block1'][18]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE19_LOTTERY = self.player.participant.vars['block1'][18]['NUMBER']
        self.player.BLOCK1_TABLE19_TYPE = self.player.participant.vars['block1'][18]['TYPE']
        self.player.BLOCK1_TABLE19_ORDER = self.player.participant.vars['block1'][18]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 19: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE19_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE19_SP_DECISION



class Block1Table20(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE20_LOTTERY',
        'BLOCK1_TABLE20_TYPE',
        'BLOCK1_TABLE20_ORDER',
        'BLOCK1_TABLE20_SP_OPTION',
        'BLOCK1_TABLE20_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=20,
            TYPE=self.player.participant.vars['block1'][19]['TYPE'],
            ORDER=self.player.participant.vars['block1'][19]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE20_LOTTERY = self.player.participant.vars['block1'][19]['NUMBER']
        self.player.BLOCK1_TABLE20_TYPE = self.player.participant.vars['block1'][19]['TYPE']
        self.player.BLOCK1_TABLE20_ORDER = self.player.participant.vars['block1'][19]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 20: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE20_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE20_SP_DECISION



class Block1Table21(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE21_LOTTERY',
        'BLOCK1_TABLE21_TYPE',
        'BLOCK1_TABLE21_ORDER',
        'BLOCK1_TABLE21_SP_OPTION',
        'BLOCK1_TABLE21_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=21,
            TYPE=self.player.participant.vars['block1'][20]['TYPE'],
            ORDER=self.player.participant.vars['block1'][20]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE21_LOTTERY = self.player.participant.vars['block1'][20]['NUMBER']
        self.player.BLOCK1_TABLE21_TYPE = self.player.participant.vars['block1'][20]['TYPE']
        self.player.BLOCK1_TABLE21_ORDER = self.player.participant.vars['block1'][20]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 21: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE21_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE21_SP_DECISION



class Block1Table22(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE22_LOTTERY',
        'BLOCK1_TABLE22_TYPE',
        'BLOCK1_TABLE22_ORDER',
        'BLOCK1_TABLE22_SP_OPTION',
        'BLOCK1_TABLE22_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=22,
            TYPE=self.player.participant.vars['block1'][21]['TYPE'],
            ORDER=self.player.participant.vars['block1'][21]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE22_LOTTERY = self.player.participant.vars['block1'][21]['NUMBER']
        self.player.BLOCK1_TABLE22_TYPE = self.player.participant.vars['block1'][21]['TYPE']
        self.player.BLOCK1_TABLE22_ORDER = self.player.participant.vars['block1'][21]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 22: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE22_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE22_SP_DECISION



class Block1Table23(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE23_LOTTERY',
        'BLOCK1_TABLE23_TYPE',
        'BLOCK1_TABLE23_ORDER',
        'BLOCK1_TABLE23_SP_OPTION',
        'BLOCK1_TABLE23_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=23,
            TYPE=self.player.participant.vars['block1'][22]['TYPE'],
            ORDER=self.player.participant.vars['block1'][22]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE23_LOTTERY = self.player.participant.vars['block1'][22]['NUMBER']
        self.player.BLOCK1_TABLE23_TYPE = self.player.participant.vars['block1'][22]['TYPE']
        self.player.BLOCK1_TABLE23_ORDER = self.player.participant.vars['block1'][22]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 23: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE23_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE23_SP_DECISION



class Block1Table24(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE24_LOTTERY',
        'BLOCK1_TABLE24_TYPE',
        'BLOCK1_TABLE24_ORDER',
        'BLOCK1_TABLE24_SP_OPTION',
        'BLOCK1_TABLE24_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=24,
            TYPE=self.player.participant.vars['block1'][23]['TYPE'],
            ORDER=self.player.participant.vars['block1'][23]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE24_LOTTERY = self.player.participant.vars['block1'][23]['NUMBER']
        self.player.BLOCK1_TABLE24_TYPE = self.player.participant.vars['block1'][23]['TYPE']
        self.player.BLOCK1_TABLE24_ORDER = self.player.participant.vars['block1'][23]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 24: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE24_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE24_SP_DECISION



class Block1Table25(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE25_LOTTERY',
        'BLOCK1_TABLE25_TYPE',
        'BLOCK1_TABLE25_ORDER',
        'BLOCK1_TABLE25_SP_OPTION',
        'BLOCK1_TABLE25_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=25,
            TYPE=self.player.participant.vars['block1'][24]['TYPE'],
            ORDER=self.player.participant.vars['block1'][24]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE25_LOTTERY = self.player.participant.vars['block1'][24]['NUMBER']
        self.player.BLOCK1_TABLE25_TYPE = self.player.participant.vars['block1'][24]['TYPE']
        self.player.BLOCK1_TABLE25_ORDER = self.player.participant.vars['block1'][24]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 25: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE25_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE25_SP_DECISION



class Block1Table26(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE26_LOTTERY',
        'BLOCK1_TABLE26_TYPE',
        'BLOCK1_TABLE26_ORDER',
        'BLOCK1_TABLE26_SP_OPTION',
        'BLOCK1_TABLE26_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=26,
            TYPE=self.player.participant.vars['block1'][25]['TYPE'],
            ORDER=self.player.participant.vars['block1'][25]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE26_LOTTERY = self.player.participant.vars['block1'][25]['NUMBER']
        self.player.BLOCK1_TABLE26_TYPE = self.player.participant.vars['block1'][25]['TYPE']
        self.player.BLOCK1_TABLE26_ORDER = self.player.participant.vars['block1'][25]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 26: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE26_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE26_SP_DECISION



class Block1Table27(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE27_LOTTERY',
        'BLOCK1_TABLE27_TYPE',
        'BLOCK1_TABLE27_ORDER',
        'BLOCK1_TABLE27_SP_OPTION',
        'BLOCK1_TABLE27_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=27,
            TYPE=self.player.participant.vars['block1'][26]['TYPE'],
            ORDER=self.player.participant.vars['block1'][26]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE27_LOTTERY = self.player.participant.vars['block1'][26]['NUMBER']
        self.player.BLOCK1_TABLE27_TYPE = self.player.participant.vars['block1'][26]['TYPE']
        self.player.BLOCK1_TABLE27_ORDER = self.player.participant.vars['block1'][26]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 27: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE27_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE27_SP_DECISION



class Block1Table28(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE28_LOTTERY',
        'BLOCK1_TABLE28_TYPE',
        'BLOCK1_TABLE28_ORDER',
        'BLOCK1_TABLE28_SP_OPTION',
        'BLOCK1_TABLE28_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=28,
            TYPE=self.player.participant.vars['block1'][27]['TYPE'],
            ORDER=self.player.participant.vars['block1'][27]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE28_LOTTERY = self.player.participant.vars['block1'][27]['NUMBER']
        self.player.BLOCK1_TABLE28_TYPE = self.player.participant.vars['block1'][27]['TYPE']
        self.player.BLOCK1_TABLE28_ORDER = self.player.participant.vars['block1'][27]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 28: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE28_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE28_SP_DECISION



class Block1Table29(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE29_LOTTERY',
        'BLOCK1_TABLE29_TYPE',
        'BLOCK1_TABLE29_ORDER',
        'BLOCK1_TABLE29_SP_OPTION',
        'BLOCK1_TABLE29_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=29,
            TYPE=self.player.participant.vars['block1'][28]['TYPE'],
            ORDER=self.player.participant.vars['block1'][28]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE29_LOTTERY = self.player.participant.vars['block1'][28]['NUMBER']
        self.player.BLOCK1_TABLE29_TYPE = self.player.participant.vars['block1'][28]['TYPE']
        self.player.BLOCK1_TABLE29_ORDER = self.player.participant.vars['block1'][28]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 29: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE29_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE29_SP_DECISION



class Block1Table30(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE30_LOTTERY',
        'BLOCK1_TABLE30_TYPE',
        'BLOCK1_TABLE30_ORDER',
        'BLOCK1_TABLE30_SP_OPTION',
        'BLOCK1_TABLE30_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=30,
            TYPE=self.player.participant.vars['block1'][29]['TYPE'],
            ORDER=self.player.participant.vars['block1'][29]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE30_LOTTERY = self.player.participant.vars['block1'][29]['NUMBER']
        self.player.BLOCK1_TABLE30_TYPE = self.player.participant.vars['block1'][29]['TYPE']
        self.player.BLOCK1_TABLE30_ORDER = self.player.participant.vars['block1'][29]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 30: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE30_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE30_SP_DECISION



class Block1Table31(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE31_LOTTERY',
        'BLOCK1_TABLE31_TYPE',
        'BLOCK1_TABLE31_ORDER',
        'BLOCK1_TABLE31_SP_OPTION',
        'BLOCK1_TABLE31_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=31,
            TYPE=self.player.participant.vars['block1'][30]['TYPE'],
            ORDER=self.player.participant.vars['block1'][30]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE31_LOTTERY = self.player.participant.vars['block1'][30]['NUMBER']
        self.player.BLOCK1_TABLE31_TYPE = self.player.participant.vars['block1'][30]['TYPE']
        self.player.BLOCK1_TABLE31_ORDER = self.player.participant.vars['block1'][30]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 31: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE31_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE31_SP_DECISION



class Block1Table32(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE32_LOTTERY',
        'BLOCK1_TABLE32_TYPE',
        'BLOCK1_TABLE32_ORDER',
        'BLOCK1_TABLE32_SP_OPTION',
        'BLOCK1_TABLE32_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=32,
            TYPE=self.player.participant.vars['block1'][31]['TYPE'],
            ORDER=self.player.participant.vars['block1'][31]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE32_LOTTERY = self.player.participant.vars['block1'][31]['NUMBER']
        self.player.BLOCK1_TABLE32_TYPE = self.player.participant.vars['block1'][31]['TYPE']
        self.player.BLOCK1_TABLE32_ORDER = self.player.participant.vars['block1'][31]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 32: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE32_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE32_SP_DECISION



class Block1Table33(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE33_LOTTERY',
        'BLOCK1_TABLE33_TYPE',
        'BLOCK1_TABLE33_ORDER',
        'BLOCK1_TABLE33_SP_OPTION',
        'BLOCK1_TABLE33_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=33,
            TYPE=self.player.participant.vars['block1'][32]['TYPE'],
            ORDER=self.player.participant.vars['block1'][32]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE33_LOTTERY = self.player.participant.vars['block1'][32]['NUMBER']
        self.player.BLOCK1_TABLE33_TYPE = self.player.participant.vars['block1'][32]['TYPE']
        self.player.BLOCK1_TABLE33_ORDER = self.player.participant.vars['block1'][32]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 33: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE33_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE33_SP_DECISION



class Block1Table34(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE34_LOTTERY',
        'BLOCK1_TABLE34_TYPE',
        'BLOCK1_TABLE34_ORDER',
        'BLOCK1_TABLE34_SP_OPTION',
        'BLOCK1_TABLE34_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=34,
            TYPE=self.player.participant.vars['block1'][33]['TYPE'],
            ORDER=self.player.participant.vars['block1'][33]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE34_LOTTERY = self.player.participant.vars['block1'][33]['NUMBER']
        self.player.BLOCK1_TABLE34_TYPE = self.player.participant.vars['block1'][33]['TYPE']
        self.player.BLOCK1_TABLE34_ORDER = self.player.participant.vars['block1'][33]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 34: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE34_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE34_SP_DECISION



class Block1Table35(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE35_LOTTERY',
        'BLOCK1_TABLE35_TYPE',
        'BLOCK1_TABLE35_ORDER',
        'BLOCK1_TABLE35_SP_OPTION',
        'BLOCK1_TABLE35_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=35,
            TYPE=self.player.participant.vars['block1'][34]['TYPE'],
            ORDER=self.player.participant.vars['block1'][34]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE35_LOTTERY = self.player.participant.vars['block1'][34]['NUMBER']
        self.player.BLOCK1_TABLE35_TYPE = self.player.participant.vars['block1'][34]['TYPE']
        self.player.BLOCK1_TABLE35_ORDER = self.player.participant.vars['block1'][34]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 35: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE35_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE35_SP_DECISION



class Block1Table36(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE36_LOTTERY',
        'BLOCK1_TABLE36_TYPE',
        'BLOCK1_TABLE36_ORDER',
        'BLOCK1_TABLE36_SP_OPTION',
        'BLOCK1_TABLE36_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=36,
            TYPE=self.player.participant.vars['block1'][35]['TYPE'],
            ORDER=self.player.participant.vars['block1'][35]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE36_LOTTERY = self.player.participant.vars['block1'][35]['NUMBER']
        self.player.BLOCK1_TABLE36_TYPE = self.player.participant.vars['block1'][35]['TYPE']
        self.player.BLOCK1_TABLE36_ORDER = self.player.participant.vars['block1'][35]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 36: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE36_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE36_SP_DECISION



class Block1Table37(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE37_LOTTERY',
        'BLOCK1_TABLE37_TYPE',
        'BLOCK1_TABLE37_ORDER',
        'BLOCK1_TABLE37_SP_OPTION',
        'BLOCK1_TABLE37_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=37,
            TYPE=self.player.participant.vars['block1'][36]['TYPE'],
            ORDER=self.player.participant.vars['block1'][36]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE37_LOTTERY = self.player.participant.vars['block1'][36]['NUMBER']
        self.player.BLOCK1_TABLE37_TYPE = self.player.participant.vars['block1'][36]['TYPE']
        self.player.BLOCK1_TABLE37_ORDER = self.player.participant.vars['block1'][36]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 37: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE37_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE37_SP_DECISION



class Block1Table38(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE38_LOTTERY',
        'BLOCK1_TABLE38_TYPE',
        'BLOCK1_TABLE38_ORDER',
        'BLOCK1_TABLE38_SP_OPTION',
        'BLOCK1_TABLE38_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=38,
            TYPE=self.player.participant.vars['block1'][37]['TYPE'],
            ORDER=self.player.participant.vars['block1'][37]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE38_LOTTERY = self.player.participant.vars['block1'][37]['NUMBER']
        self.player.BLOCK1_TABLE38_TYPE = self.player.participant.vars['block1'][37]['TYPE']
        self.player.BLOCK1_TABLE38_ORDER = self.player.participant.vars['block1'][37]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 38: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE38_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE38_SP_DECISION



class Block1Table39(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE39_LOTTERY',
        'BLOCK1_TABLE39_TYPE',
        'BLOCK1_TABLE39_ORDER',
        'BLOCK1_TABLE39_SP_OPTION',
        'BLOCK1_TABLE39_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=39,
            TYPE=self.player.participant.vars['block1'][38]['TYPE'],
            ORDER=self.player.participant.vars['block1'][38]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE39_LOTTERY = self.player.participant.vars['block1'][38]['NUMBER']
        self.player.BLOCK1_TABLE39_TYPE = self.player.participant.vars['block1'][38]['TYPE']
        self.player.BLOCK1_TABLE39_ORDER = self.player.participant.vars['block1'][38]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 39: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE39_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE39_SP_DECISION



class Block1Table40(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK1_TABLE40_LOTTERY',
        'BLOCK1_TABLE40_TYPE',
        'BLOCK1_TABLE40_ORDER',
        'BLOCK1_TABLE40_SP_OPTION',
        'BLOCK1_TABLE40_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=1,
            TABLE_NUMBER=40,
            TYPE=self.player.participant.vars['block1'][39]['TYPE'],
            ORDER=self.player.participant.vars['block1'][39]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK1_TABLE40_LOTTERY = self.player.participant.vars['block1'][39]['NUMBER']
        self.player.BLOCK1_TABLE40_TYPE = self.player.participant.vars['block1'][39]['TYPE']
        self.player.BLOCK1_TABLE40_ORDER = self.player.participant.vars['block1'][39]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 1) and self.player.participant.vars['payoff_random_table'] == 40: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK1_TABLE40_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK1_TABLE40_SP_DECISION



class ZwischenteilIntro(Page):
    pass
    

class Zwischenteil1(Page):
    form_model = 'player'
    form_fields = ['ZWISCHENFRAGE7']
    

class Zwischenteil2(Page):
    form_model = 'player'
    form_fields = ['ZWISCHENFRAGE4']
    

class Zwischenteil3(Page):
    form_model = 'player'
    form_fields = ['ZWISCHENFRAGE5']
    

class Zwischenteil4(Page):
    form_model = 'player'
    form_fields = ['ZWISCHENFRAGE9']
    

class Zwischenteil5(Page):
    form_model = 'player'
    form_fields = ['ZWISCHENFRAGE10']
    

class Zwischenteil6(Page):
    form_model = 'player'
    form_fields = ['ZWISCHENFRAGE12']
    

class Zwischenteil7(Page):
    form_model = 'player'
    form_fields = ['ZWISCHENFRAGE8']
    

class Zwischenteil8(Page):
    form_model = 'player'
    form_fields = ['ZWISCHENFRAGE15']
    

class Zwischenteil9(Page):
    form_model = 'player'
    form_fields = ['ZWISCHENFRAGE11']
    

class Zwischenteil10(Page):
    form_model = 'player'
    form_fields = ['ZWISCHENFRAGE13']
    

class Zwischenteil11(Page):
    form_model = 'player'
    form_fields = ['ZWISCHENFRAGE2']
    

class Zwischenteil12(Page):
    form_model = 'player'
    form_fields = ['ZWISCHENFRAGE16']
    

class Zwischenteil13(Page):
    form_model = 'player'
    form_fields = ['ZWISCHENFRAGE14']
    

class Zwischenteil14(Page):
    form_model = 'player'
    form_fields = ['ZWISCHENFRAGE1']
    

class Zwischenteil15(Page):
    form_model = 'player'
    form_fields = ['ZWISCHENFRAGE3']
    

class Zwischenteil16(Page):
    form_model = 'player'
    form_fields = ['ZWISCHENFRAGE6']
    

class Block2Intro(Page):
    def vars_for_template(self):
        self.player.participant.vars['block2'] = self.player.getBlock(2)

class Block2Table1(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE1_LOTTERY',
        'BLOCK2_TABLE1_TYPE',
        'BLOCK2_TABLE1_ORDER',
        'BLOCK2_TABLE1_SP_OPTION',
        'BLOCK2_TABLE1_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=1,
            TYPE=self.player.participant.vars['block2'][0]['TYPE'],
            ORDER=self.player.participant.vars['block2'][0]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE1_LOTTERY = self.player.participant.vars['block2'][0]['NUMBER']
        self.player.BLOCK2_TABLE1_TYPE = self.player.participant.vars['block2'][0]['TYPE']
        self.player.BLOCK2_TABLE1_ORDER = self.player.participant.vars['block2'][0]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 1: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE1_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE1_SP_DECISION



class Block2Table2(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE2_LOTTERY',
        'BLOCK2_TABLE2_TYPE',
        'BLOCK2_TABLE2_ORDER',
        'BLOCK2_TABLE2_SP_OPTION',
        'BLOCK2_TABLE2_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=2,
            TYPE=self.player.participant.vars['block2'][1]['TYPE'],
            ORDER=self.player.participant.vars['block2'][1]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE2_LOTTERY = self.player.participant.vars['block2'][1]['NUMBER']
        self.player.BLOCK2_TABLE2_TYPE = self.player.participant.vars['block2'][1]['TYPE']
        self.player.BLOCK2_TABLE2_ORDER = self.player.participant.vars['block2'][1]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 2: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE2_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE2_SP_DECISION



class Block2Table3(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE3_LOTTERY',
        'BLOCK2_TABLE3_TYPE',
        'BLOCK2_TABLE3_ORDER',
        'BLOCK2_TABLE3_SP_OPTION',
        'BLOCK2_TABLE3_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=3,
            TYPE=self.player.participant.vars['block2'][2]['TYPE'],
            ORDER=self.player.participant.vars['block2'][2]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE3_LOTTERY = self.player.participant.vars['block2'][2]['NUMBER']
        self.player.BLOCK2_TABLE3_TYPE = self.player.participant.vars['block2'][2]['TYPE']
        self.player.BLOCK2_TABLE3_ORDER = self.player.participant.vars['block2'][2]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 3: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE3_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE3_SP_DECISION



class Block2Table4(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE4_LOTTERY',
        'BLOCK2_TABLE4_TYPE',
        'BLOCK2_TABLE4_ORDER',
        'BLOCK2_TABLE4_SP_OPTION',
        'BLOCK2_TABLE4_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=4,
            TYPE=self.player.participant.vars['block2'][3]['TYPE'],
            ORDER=self.player.participant.vars['block2'][3]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE4_LOTTERY = self.player.participant.vars['block2'][3]['NUMBER']
        self.player.BLOCK2_TABLE4_TYPE = self.player.participant.vars['block2'][3]['TYPE']
        self.player.BLOCK2_TABLE4_ORDER = self.player.participant.vars['block2'][3]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 4: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE4_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE4_SP_DECISION



class Block2Table5(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE5_LOTTERY',
        'BLOCK2_TABLE5_TYPE',
        'BLOCK2_TABLE5_ORDER',
        'BLOCK2_TABLE5_SP_OPTION',
        'BLOCK2_TABLE5_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=5,
            TYPE=self.player.participant.vars['block2'][4]['TYPE'],
            ORDER=self.player.participant.vars['block2'][4]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE5_LOTTERY = self.player.participant.vars['block2'][4]['NUMBER']
        self.player.BLOCK2_TABLE5_TYPE = self.player.participant.vars['block2'][4]['TYPE']
        self.player.BLOCK2_TABLE5_ORDER = self.player.participant.vars['block2'][4]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 5: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE5_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE5_SP_DECISION



class Block2Table6(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE6_LOTTERY',
        'BLOCK2_TABLE6_TYPE',
        'BLOCK2_TABLE6_ORDER',
        'BLOCK2_TABLE6_SP_OPTION',
        'BLOCK2_TABLE6_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=6,
            TYPE=self.player.participant.vars['block2'][5]['TYPE'],
            ORDER=self.player.participant.vars['block2'][5]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE6_LOTTERY = self.player.participant.vars['block2'][5]['NUMBER']
        self.player.BLOCK2_TABLE6_TYPE = self.player.participant.vars['block2'][5]['TYPE']
        self.player.BLOCK2_TABLE6_ORDER = self.player.participant.vars['block2'][5]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 6: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE6_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE6_SP_DECISION



class Block2Table7(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE7_LOTTERY',
        'BLOCK2_TABLE7_TYPE',
        'BLOCK2_TABLE7_ORDER',
        'BLOCK2_TABLE7_SP_OPTION',
        'BLOCK2_TABLE7_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=7,
            TYPE=self.player.participant.vars['block2'][6]['TYPE'],
            ORDER=self.player.participant.vars['block2'][6]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE7_LOTTERY = self.player.participant.vars['block2'][6]['NUMBER']
        self.player.BLOCK2_TABLE7_TYPE = self.player.participant.vars['block2'][6]['TYPE']
        self.player.BLOCK2_TABLE7_ORDER = self.player.participant.vars['block2'][6]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 7: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE7_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE7_SP_DECISION



class Block2Table8(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE8_LOTTERY',
        'BLOCK2_TABLE8_TYPE',
        'BLOCK2_TABLE8_ORDER',
        'BLOCK2_TABLE8_SP_OPTION',
        'BLOCK2_TABLE8_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=8,
            TYPE=self.player.participant.vars['block2'][7]['TYPE'],
            ORDER=self.player.participant.vars['block2'][7]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE8_LOTTERY = self.player.participant.vars['block2'][7]['NUMBER']
        self.player.BLOCK2_TABLE8_TYPE = self.player.participant.vars['block2'][7]['TYPE']
        self.player.BLOCK2_TABLE8_ORDER = self.player.participant.vars['block2'][7]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 8: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE8_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE8_SP_DECISION



class Block2Table9(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE9_LOTTERY',
        'BLOCK2_TABLE9_TYPE',
        'BLOCK2_TABLE9_ORDER',
        'BLOCK2_TABLE9_SP_OPTION',
        'BLOCK2_TABLE9_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=9,
            TYPE=self.player.participant.vars['block2'][8]['TYPE'],
            ORDER=self.player.participant.vars['block2'][8]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE9_LOTTERY = self.player.participant.vars['block2'][8]['NUMBER']
        self.player.BLOCK2_TABLE9_TYPE = self.player.participant.vars['block2'][8]['TYPE']
        self.player.BLOCK2_TABLE9_ORDER = self.player.participant.vars['block2'][8]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 9: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE9_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE9_SP_DECISION



class Block2Table10(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE10_LOTTERY',
        'BLOCK2_TABLE10_TYPE',
        'BLOCK2_TABLE10_ORDER',
        'BLOCK2_TABLE10_SP_OPTION',
        'BLOCK2_TABLE10_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=10,
            TYPE=self.player.participant.vars['block2'][9]['TYPE'],
            ORDER=self.player.participant.vars['block2'][9]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE10_LOTTERY = self.player.participant.vars['block2'][9]['NUMBER']
        self.player.BLOCK2_TABLE10_TYPE = self.player.participant.vars['block2'][9]['TYPE']
        self.player.BLOCK2_TABLE10_ORDER = self.player.participant.vars['block2'][9]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 10: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE10_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE10_SP_DECISION



class Block2Table11(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE11_LOTTERY',
        'BLOCK2_TABLE11_TYPE',
        'BLOCK2_TABLE11_ORDER',
        'BLOCK2_TABLE11_SP_OPTION',
        'BLOCK2_TABLE11_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=11,
            TYPE=self.player.participant.vars['block2'][10]['TYPE'],
            ORDER=self.player.participant.vars['block2'][10]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE11_LOTTERY = self.player.participant.vars['block2'][10]['NUMBER']
        self.player.BLOCK2_TABLE11_TYPE = self.player.participant.vars['block2'][10]['TYPE']
        self.player.BLOCK2_TABLE11_ORDER = self.player.participant.vars['block2'][10]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 11: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE11_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE11_SP_DECISION



class Block2Table12(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE12_LOTTERY',
        'BLOCK2_TABLE12_TYPE',
        'BLOCK2_TABLE12_ORDER',
        'BLOCK2_TABLE12_SP_OPTION',
        'BLOCK2_TABLE12_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=12,
            TYPE=self.player.participant.vars['block2'][11]['TYPE'],
            ORDER=self.player.participant.vars['block2'][11]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE12_LOTTERY = self.player.participant.vars['block2'][11]['NUMBER']
        self.player.BLOCK2_TABLE12_TYPE = self.player.participant.vars['block2'][11]['TYPE']
        self.player.BLOCK2_TABLE12_ORDER = self.player.participant.vars['block2'][11]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 12: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE12_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE12_SP_DECISION



class Block2Table13(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE13_LOTTERY',
        'BLOCK2_TABLE13_TYPE',
        'BLOCK2_TABLE13_ORDER',
        'BLOCK2_TABLE13_SP_OPTION',
        'BLOCK2_TABLE13_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=13,
            TYPE=self.player.participant.vars['block2'][12]['TYPE'],
            ORDER=self.player.participant.vars['block2'][12]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE13_LOTTERY = self.player.participant.vars['block2'][12]['NUMBER']
        self.player.BLOCK2_TABLE13_TYPE = self.player.participant.vars['block2'][12]['TYPE']
        self.player.BLOCK2_TABLE13_ORDER = self.player.participant.vars['block2'][12]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 13: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE13_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE13_SP_DECISION



class Block2Table14(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE14_LOTTERY',
        'BLOCK2_TABLE14_TYPE',
        'BLOCK2_TABLE14_ORDER',
        'BLOCK2_TABLE14_SP_OPTION',
        'BLOCK2_TABLE14_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=14,
            TYPE=self.player.participant.vars['block2'][13]['TYPE'],
            ORDER=self.player.participant.vars['block2'][13]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE14_LOTTERY = self.player.participant.vars['block2'][13]['NUMBER']
        self.player.BLOCK2_TABLE14_TYPE = self.player.participant.vars['block2'][13]['TYPE']
        self.player.BLOCK2_TABLE14_ORDER = self.player.participant.vars['block2'][13]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 14: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE14_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE14_SP_DECISION



class Block2Table15(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE15_LOTTERY',
        'BLOCK2_TABLE15_TYPE',
        'BLOCK2_TABLE15_ORDER',
        'BLOCK2_TABLE15_SP_OPTION',
        'BLOCK2_TABLE15_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=15,
            TYPE=self.player.participant.vars['block2'][14]['TYPE'],
            ORDER=self.player.participant.vars['block2'][14]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE15_LOTTERY = self.player.participant.vars['block2'][14]['NUMBER']
        self.player.BLOCK2_TABLE15_TYPE = self.player.participant.vars['block2'][14]['TYPE']
        self.player.BLOCK2_TABLE15_ORDER = self.player.participant.vars['block2'][14]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 15: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE15_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE15_SP_DECISION



class Block2Table16(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE16_LOTTERY',
        'BLOCK2_TABLE16_TYPE',
        'BLOCK2_TABLE16_ORDER',
        'BLOCK2_TABLE16_SP_OPTION',
        'BLOCK2_TABLE16_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=16,
            TYPE=self.player.participant.vars['block2'][15]['TYPE'],
            ORDER=self.player.participant.vars['block2'][15]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE16_LOTTERY = self.player.participant.vars['block2'][15]['NUMBER']
        self.player.BLOCK2_TABLE16_TYPE = self.player.participant.vars['block2'][15]['TYPE']
        self.player.BLOCK2_TABLE16_ORDER = self.player.participant.vars['block2'][15]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 16: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE16_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE16_SP_DECISION



class Block2Table17(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE17_LOTTERY',
        'BLOCK2_TABLE17_TYPE',
        'BLOCK2_TABLE17_ORDER',
        'BLOCK2_TABLE17_SP_OPTION',
        'BLOCK2_TABLE17_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=17,
            TYPE=self.player.participant.vars['block2'][16]['TYPE'],
            ORDER=self.player.participant.vars['block2'][16]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE17_LOTTERY = self.player.participant.vars['block2'][16]['NUMBER']
        self.player.BLOCK2_TABLE17_TYPE = self.player.participant.vars['block2'][16]['TYPE']
        self.player.BLOCK2_TABLE17_ORDER = self.player.participant.vars['block2'][16]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 17: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE17_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE17_SP_DECISION



class Block2Table18(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE18_LOTTERY',
        'BLOCK2_TABLE18_TYPE',
        'BLOCK2_TABLE18_ORDER',
        'BLOCK2_TABLE18_SP_OPTION',
        'BLOCK2_TABLE18_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=18,
            TYPE=self.player.participant.vars['block2'][17]['TYPE'],
            ORDER=self.player.participant.vars['block2'][17]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE18_LOTTERY = self.player.participant.vars['block2'][17]['NUMBER']
        self.player.BLOCK2_TABLE18_TYPE = self.player.participant.vars['block2'][17]['TYPE']
        self.player.BLOCK2_TABLE18_ORDER = self.player.participant.vars['block2'][17]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 18: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE18_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE18_SP_DECISION



class Block2Table19(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE19_LOTTERY',
        'BLOCK2_TABLE19_TYPE',
        'BLOCK2_TABLE19_ORDER',
        'BLOCK2_TABLE19_SP_OPTION',
        'BLOCK2_TABLE19_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=19,
            TYPE=self.player.participant.vars['block2'][18]['TYPE'],
            ORDER=self.player.participant.vars['block2'][18]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE19_LOTTERY = self.player.participant.vars['block2'][18]['NUMBER']
        self.player.BLOCK2_TABLE19_TYPE = self.player.participant.vars['block2'][18]['TYPE']
        self.player.BLOCK2_TABLE19_ORDER = self.player.participant.vars['block2'][18]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 19: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE19_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE19_SP_DECISION



class Block2Table20(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE20_LOTTERY',
        'BLOCK2_TABLE20_TYPE',
        'BLOCK2_TABLE20_ORDER',
        'BLOCK2_TABLE20_SP_OPTION',
        'BLOCK2_TABLE20_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=20,
            TYPE=self.player.participant.vars['block2'][19]['TYPE'],
            ORDER=self.player.participant.vars['block2'][19]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE20_LOTTERY = self.player.participant.vars['block2'][19]['NUMBER']
        self.player.BLOCK2_TABLE20_TYPE = self.player.participant.vars['block2'][19]['TYPE']
        self.player.BLOCK2_TABLE20_ORDER = self.player.participant.vars['block2'][19]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 20: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE20_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE20_SP_DECISION



class Block2Table21(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE21_LOTTERY',
        'BLOCK2_TABLE21_TYPE',
        'BLOCK2_TABLE21_ORDER',
        'BLOCK2_TABLE21_SP_OPTION',
        'BLOCK2_TABLE21_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=21,
            TYPE=self.player.participant.vars['block2'][20]['TYPE'],
            ORDER=self.player.participant.vars['block2'][20]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE21_LOTTERY = self.player.participant.vars['block2'][20]['NUMBER']
        self.player.BLOCK2_TABLE21_TYPE = self.player.participant.vars['block2'][20]['TYPE']
        self.player.BLOCK2_TABLE21_ORDER = self.player.participant.vars['block2'][20]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 21: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE21_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE21_SP_DECISION



class Block2Table22(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE22_LOTTERY',
        'BLOCK2_TABLE22_TYPE',
        'BLOCK2_TABLE22_ORDER',
        'BLOCK2_TABLE22_SP_OPTION',
        'BLOCK2_TABLE22_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=22,
            TYPE=self.player.participant.vars['block2'][21]['TYPE'],
            ORDER=self.player.participant.vars['block2'][21]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE22_LOTTERY = self.player.participant.vars['block2'][21]['NUMBER']
        self.player.BLOCK2_TABLE22_TYPE = self.player.participant.vars['block2'][21]['TYPE']
        self.player.BLOCK2_TABLE22_ORDER = self.player.participant.vars['block2'][21]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 22: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE22_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE22_SP_DECISION



class Block2Table23(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE23_LOTTERY',
        'BLOCK2_TABLE23_TYPE',
        'BLOCK2_TABLE23_ORDER',
        'BLOCK2_TABLE23_SP_OPTION',
        'BLOCK2_TABLE23_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=23,
            TYPE=self.player.participant.vars['block2'][22]['TYPE'],
            ORDER=self.player.participant.vars['block2'][22]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE23_LOTTERY = self.player.participant.vars['block2'][22]['NUMBER']
        self.player.BLOCK2_TABLE23_TYPE = self.player.participant.vars['block2'][22]['TYPE']
        self.player.BLOCK2_TABLE23_ORDER = self.player.participant.vars['block2'][22]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 23: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE23_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE23_SP_DECISION



class Block2Table24(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE24_LOTTERY',
        'BLOCK2_TABLE24_TYPE',
        'BLOCK2_TABLE24_ORDER',
        'BLOCK2_TABLE24_SP_OPTION',
        'BLOCK2_TABLE24_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=24,
            TYPE=self.player.participant.vars['block2'][23]['TYPE'],
            ORDER=self.player.participant.vars['block2'][23]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE24_LOTTERY = self.player.participant.vars['block2'][23]['NUMBER']
        self.player.BLOCK2_TABLE24_TYPE = self.player.participant.vars['block2'][23]['TYPE']
        self.player.BLOCK2_TABLE24_ORDER = self.player.participant.vars['block2'][23]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 24: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE24_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE24_SP_DECISION



class Block2Table25(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE25_LOTTERY',
        'BLOCK2_TABLE25_TYPE',
        'BLOCK2_TABLE25_ORDER',
        'BLOCK2_TABLE25_SP_OPTION',
        'BLOCK2_TABLE25_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=25,
            TYPE=self.player.participant.vars['block2'][24]['TYPE'],
            ORDER=self.player.participant.vars['block2'][24]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE25_LOTTERY = self.player.participant.vars['block2'][24]['NUMBER']
        self.player.BLOCK2_TABLE25_TYPE = self.player.participant.vars['block2'][24]['TYPE']
        self.player.BLOCK2_TABLE25_ORDER = self.player.participant.vars['block2'][24]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 25: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE25_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE25_SP_DECISION



class Block2Table26(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE26_LOTTERY',
        'BLOCK2_TABLE26_TYPE',
        'BLOCK2_TABLE26_ORDER',
        'BLOCK2_TABLE26_SP_OPTION',
        'BLOCK2_TABLE26_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=26,
            TYPE=self.player.participant.vars['block2'][25]['TYPE'],
            ORDER=self.player.participant.vars['block2'][25]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE26_LOTTERY = self.player.participant.vars['block2'][25]['NUMBER']
        self.player.BLOCK2_TABLE26_TYPE = self.player.participant.vars['block2'][25]['TYPE']
        self.player.BLOCK2_TABLE26_ORDER = self.player.participant.vars['block2'][25]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 26: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE26_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE26_SP_DECISION



class Block2Table27(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE27_LOTTERY',
        'BLOCK2_TABLE27_TYPE',
        'BLOCK2_TABLE27_ORDER',
        'BLOCK2_TABLE27_SP_OPTION',
        'BLOCK2_TABLE27_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=27,
            TYPE=self.player.participant.vars['block2'][26]['TYPE'],
            ORDER=self.player.participant.vars['block2'][26]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE27_LOTTERY = self.player.participant.vars['block2'][26]['NUMBER']
        self.player.BLOCK2_TABLE27_TYPE = self.player.participant.vars['block2'][26]['TYPE']
        self.player.BLOCK2_TABLE27_ORDER = self.player.participant.vars['block2'][26]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 27: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE27_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE27_SP_DECISION



class Block2Table28(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE28_LOTTERY',
        'BLOCK2_TABLE28_TYPE',
        'BLOCK2_TABLE28_ORDER',
        'BLOCK2_TABLE28_SP_OPTION',
        'BLOCK2_TABLE28_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=28,
            TYPE=self.player.participant.vars['block2'][27]['TYPE'],
            ORDER=self.player.participant.vars['block2'][27]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE28_LOTTERY = self.player.participant.vars['block2'][27]['NUMBER']
        self.player.BLOCK2_TABLE28_TYPE = self.player.participant.vars['block2'][27]['TYPE']
        self.player.BLOCK2_TABLE28_ORDER = self.player.participant.vars['block2'][27]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 28: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE28_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE28_SP_DECISION



class Block2Table29(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE29_LOTTERY',
        'BLOCK2_TABLE29_TYPE',
        'BLOCK2_TABLE29_ORDER',
        'BLOCK2_TABLE29_SP_OPTION',
        'BLOCK2_TABLE29_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=29,
            TYPE=self.player.participant.vars['block2'][28]['TYPE'],
            ORDER=self.player.participant.vars['block2'][28]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE29_LOTTERY = self.player.participant.vars['block2'][28]['NUMBER']
        self.player.BLOCK2_TABLE29_TYPE = self.player.participant.vars['block2'][28]['TYPE']
        self.player.BLOCK2_TABLE29_ORDER = self.player.participant.vars['block2'][28]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 29: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE29_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE29_SP_DECISION



class Block2Table30(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE30_LOTTERY',
        'BLOCK2_TABLE30_TYPE',
        'BLOCK2_TABLE30_ORDER',
        'BLOCK2_TABLE30_SP_OPTION',
        'BLOCK2_TABLE30_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=30,
            TYPE=self.player.participant.vars['block2'][29]['TYPE'],
            ORDER=self.player.participant.vars['block2'][29]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE30_LOTTERY = self.player.participant.vars['block2'][29]['NUMBER']
        self.player.BLOCK2_TABLE30_TYPE = self.player.participant.vars['block2'][29]['TYPE']
        self.player.BLOCK2_TABLE30_ORDER = self.player.participant.vars['block2'][29]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 30: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE30_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE30_SP_DECISION



class Block2Table31(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE31_LOTTERY',
        'BLOCK2_TABLE31_TYPE',
        'BLOCK2_TABLE31_ORDER',
        'BLOCK2_TABLE31_SP_OPTION',
        'BLOCK2_TABLE31_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=31,
            TYPE=self.player.participant.vars['block2'][30]['TYPE'],
            ORDER=self.player.participant.vars['block2'][30]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE31_LOTTERY = self.player.participant.vars['block2'][30]['NUMBER']
        self.player.BLOCK2_TABLE31_TYPE = self.player.participant.vars['block2'][30]['TYPE']
        self.player.BLOCK2_TABLE31_ORDER = self.player.participant.vars['block2'][30]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 31: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE31_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE31_SP_DECISION



class Block2Table32(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE32_LOTTERY',
        'BLOCK2_TABLE32_TYPE',
        'BLOCK2_TABLE32_ORDER',
        'BLOCK2_TABLE32_SP_OPTION',
        'BLOCK2_TABLE32_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=32,
            TYPE=self.player.participant.vars['block2'][31]['TYPE'],
            ORDER=self.player.participant.vars['block2'][31]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE32_LOTTERY = self.player.participant.vars['block2'][31]['NUMBER']
        self.player.BLOCK2_TABLE32_TYPE = self.player.participant.vars['block2'][31]['TYPE']
        self.player.BLOCK2_TABLE32_ORDER = self.player.participant.vars['block2'][31]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 32: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE32_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE32_SP_DECISION



class Block2Table33(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE33_LOTTERY',
        'BLOCK2_TABLE33_TYPE',
        'BLOCK2_TABLE33_ORDER',
        'BLOCK2_TABLE33_SP_OPTION',
        'BLOCK2_TABLE33_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=33,
            TYPE=self.player.participant.vars['block2'][32]['TYPE'],
            ORDER=self.player.participant.vars['block2'][32]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE33_LOTTERY = self.player.participant.vars['block2'][32]['NUMBER']
        self.player.BLOCK2_TABLE33_TYPE = self.player.participant.vars['block2'][32]['TYPE']
        self.player.BLOCK2_TABLE33_ORDER = self.player.participant.vars['block2'][32]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 33: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE33_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE33_SP_DECISION



class Block2Table34(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE34_LOTTERY',
        'BLOCK2_TABLE34_TYPE',
        'BLOCK2_TABLE34_ORDER',
        'BLOCK2_TABLE34_SP_OPTION',
        'BLOCK2_TABLE34_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=34,
            TYPE=self.player.participant.vars['block2'][33]['TYPE'],
            ORDER=self.player.participant.vars['block2'][33]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE34_LOTTERY = self.player.participant.vars['block2'][33]['NUMBER']
        self.player.BLOCK2_TABLE34_TYPE = self.player.participant.vars['block2'][33]['TYPE']
        self.player.BLOCK2_TABLE34_ORDER = self.player.participant.vars['block2'][33]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 34: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE34_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE34_SP_DECISION



class Block2Table35(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE35_LOTTERY',
        'BLOCK2_TABLE35_TYPE',
        'BLOCK2_TABLE35_ORDER',
        'BLOCK2_TABLE35_SP_OPTION',
        'BLOCK2_TABLE35_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=35,
            TYPE=self.player.participant.vars['block2'][34]['TYPE'],
            ORDER=self.player.participant.vars['block2'][34]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE35_LOTTERY = self.player.participant.vars['block2'][34]['NUMBER']
        self.player.BLOCK2_TABLE35_TYPE = self.player.participant.vars['block2'][34]['TYPE']
        self.player.BLOCK2_TABLE35_ORDER = self.player.participant.vars['block2'][34]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 35: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE35_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE35_SP_DECISION



class Block2Table36(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE36_LOTTERY',
        'BLOCK2_TABLE36_TYPE',
        'BLOCK2_TABLE36_ORDER',
        'BLOCK2_TABLE36_SP_OPTION',
        'BLOCK2_TABLE36_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=36,
            TYPE=self.player.participant.vars['block2'][35]['TYPE'],
            ORDER=self.player.participant.vars['block2'][35]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE36_LOTTERY = self.player.participant.vars['block2'][35]['NUMBER']
        self.player.BLOCK2_TABLE36_TYPE = self.player.participant.vars['block2'][35]['TYPE']
        self.player.BLOCK2_TABLE36_ORDER = self.player.participant.vars['block2'][35]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 36: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE36_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE36_SP_DECISION



class Block2Table37(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE37_LOTTERY',
        'BLOCK2_TABLE37_TYPE',
        'BLOCK2_TABLE37_ORDER',
        'BLOCK2_TABLE37_SP_OPTION',
        'BLOCK2_TABLE37_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=37,
            TYPE=self.player.participant.vars['block2'][36]['TYPE'],
            ORDER=self.player.participant.vars['block2'][36]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE37_LOTTERY = self.player.participant.vars['block2'][36]['NUMBER']
        self.player.BLOCK2_TABLE37_TYPE = self.player.participant.vars['block2'][36]['TYPE']
        self.player.BLOCK2_TABLE37_ORDER = self.player.participant.vars['block2'][36]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 37: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE37_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE37_SP_DECISION



class Block2Table38(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE38_LOTTERY',
        'BLOCK2_TABLE38_TYPE',
        'BLOCK2_TABLE38_ORDER',
        'BLOCK2_TABLE38_SP_OPTION',
        'BLOCK2_TABLE38_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=38,
            TYPE=self.player.participant.vars['block2'][37]['TYPE'],
            ORDER=self.player.participant.vars['block2'][37]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE38_LOTTERY = self.player.participant.vars['block2'][37]['NUMBER']
        self.player.BLOCK2_TABLE38_TYPE = self.player.participant.vars['block2'][37]['TYPE']
        self.player.BLOCK2_TABLE38_ORDER = self.player.participant.vars['block2'][37]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 38: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE38_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE38_SP_DECISION



class Block2Table39(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE39_LOTTERY',
        'BLOCK2_TABLE39_TYPE',
        'BLOCK2_TABLE39_ORDER',
        'BLOCK2_TABLE39_SP_OPTION',
        'BLOCK2_TABLE39_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=39,
            TYPE=self.player.participant.vars['block2'][38]['TYPE'],
            ORDER=self.player.participant.vars['block2'][38]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE39_LOTTERY = self.player.participant.vars['block2'][38]['NUMBER']
        self.player.BLOCK2_TABLE39_TYPE = self.player.participant.vars['block2'][38]['TYPE']
        self.player.BLOCK2_TABLE39_ORDER = self.player.participant.vars['block2'][38]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 39: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE39_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE39_SP_DECISION



class Block2Table40(Page):
    form_model = 'player'
    form_fields = [
        'BLOCK2_TABLE40_LOTTERY',
        'BLOCK2_TABLE40_TYPE',
        'BLOCK2_TABLE40_ORDER',
        'BLOCK2_TABLE40_SP_OPTION',
        'BLOCK2_TABLE40_SP_DECISION'
    ]

    def js_vars(self):
        player = self.player
        return dict(
            BLOCK_NUMBER=2,
            TABLE_NUMBER=40,
            TYPE=self.player.participant.vars['block2'][39]['TYPE'],
            ORDER=self.player.participant.vars['block2'][39]['ORDER'],
        )
        
    def before_next_page(self):
        self.player.BLOCK2_TABLE40_LOTTERY = self.player.participant.vars['block2'][39]['NUMBER']
        self.player.BLOCK2_TABLE40_TYPE = self.player.participant.vars['block2'][39]['TYPE']
        self.player.BLOCK2_TABLE40_ORDER = self.player.participant.vars['block2'][39]['ORDER']
      
        
        if (self.player.participant.vars['payoff_random_block'] == 2) and self.player.participant.vars['payoff_random_table'] == 40: 
            self.player.participant.vars['payoff_player_sp_option'] = self.player.BLOCK2_TABLE40_SP_OPTION
            self.player.participant.vars['payoff_player_sp_decision'] = self.player.BLOCK2_TABLE40_SP_DECISION



class SetPayoff(Page):
    def vars_for_template(self):
        self.player.setPayoff()    



page_sequence = [Block1Intro, Block1Table1, Block1Table2, Block1Table3, Block1Table4, Block1Table5, Block1Table6, Block1Table7, Block1Table8, Block1Table9, Block1Table10, Block1Table11, Block1Table12, Block1Table13, Block1Table14, Block1Table15, Block1Table16, Block1Table17, Block1Table18, Block1Table19, Block1Table20, Block1Table21, Block1Table22, Block1Table23, Block1Table24, Block1Table25, Block1Table26, Block1Table27, Block1Table28, Block1Table29, Block1Table30, Block1Table31, Block1Table32, Block1Table33, Block1Table34, Block1Table35, Block1Table36, Block1Table37, Block1Table38, Block1Table39, Block1Table40, ZwischenteilIntro, Zwischenteil1, Zwischenteil2, Zwischenteil3, Zwischenteil4, Zwischenteil5, Zwischenteil6, Zwischenteil7, Zwischenteil8, Zwischenteil9, Zwischenteil10, Zwischenteil11, Zwischenteil12, Zwischenteil13, Zwischenteil14, Zwischenteil15, Zwischenteil16, Block2Intro, Block2Table1, Block2Table2, Block2Table3, Block2Table4, Block2Table5, Block2Table6, Block2Table7, Block2Table8, Block2Table9, Block2Table10, Block2Table11, Block2Table12, Block2Table13, Block2Table14, Block2Table15, Block2Table16, Block2Table17, Block2Table18, Block2Table19, Block2Table20, Block2Table21, Block2Table22, Block2Table23, Block2Table24, Block2Table25, Block2Table26, Block2Table27, Block2Table28, Block2Table29, Block2Table30, Block2Table31, Block2Table32, Block2Table33, Block2Table34, Block2Table35, Block2Table36, Block2Table37, Block2Table38, Block2Table39, Block2Table40, SetPayoff]    
