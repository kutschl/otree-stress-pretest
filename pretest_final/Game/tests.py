from . import pages
from ._builtin import Bot
import random as rd


class PlayerBot(Bot):
    def play_round(self):
        
        yield pages.Block1Intro,

        yield pages.Block1Table1, dict(
            BLOCK1_TABLE1_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE1_TYPE=rd.randint(0,1),
            BLOCK1_TABLE1_ORDER=rd.randint(0,1),
            BLOCK1_TABLE1_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE1_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table2, dict(
            BLOCK1_TABLE2_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE2_TYPE=rd.randint(0,1),
            BLOCK1_TABLE2_ORDER=rd.randint(0,1),
            BLOCK1_TABLE2_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE2_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table3, dict(
            BLOCK1_TABLE3_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE3_TYPE=rd.randint(0,1),
            BLOCK1_TABLE3_ORDER=rd.randint(0,1),
            BLOCK1_TABLE3_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE3_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table4, dict(
            BLOCK1_TABLE4_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE4_TYPE=rd.randint(0,1),
            BLOCK1_TABLE4_ORDER=rd.randint(0,1),
            BLOCK1_TABLE4_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE4_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table5, dict(
            BLOCK1_TABLE5_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE5_TYPE=rd.randint(0,1),
            BLOCK1_TABLE5_ORDER=rd.randint(0,1),
            BLOCK1_TABLE5_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE5_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table6, dict(
            BLOCK1_TABLE6_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE6_TYPE=rd.randint(0,1),
            BLOCK1_TABLE6_ORDER=rd.randint(0,1),
            BLOCK1_TABLE6_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE6_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table7, dict(
            BLOCK1_TABLE7_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE7_TYPE=rd.randint(0,1),
            BLOCK1_TABLE7_ORDER=rd.randint(0,1),
            BLOCK1_TABLE7_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE7_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table8, dict(
            BLOCK1_TABLE8_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE8_TYPE=rd.randint(0,1),
            BLOCK1_TABLE8_ORDER=rd.randint(0,1),
            BLOCK1_TABLE8_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE8_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table9, dict(
            BLOCK1_TABLE9_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE9_TYPE=rd.randint(0,1),
            BLOCK1_TABLE9_ORDER=rd.randint(0,1),
            BLOCK1_TABLE9_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE9_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table10, dict(
            BLOCK1_TABLE10_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE10_TYPE=rd.randint(0,1),
            BLOCK1_TABLE10_ORDER=rd.randint(0,1),
            BLOCK1_TABLE10_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE10_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table11, dict(
            BLOCK1_TABLE11_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE11_TYPE=rd.randint(0,1),
            BLOCK1_TABLE11_ORDER=rd.randint(0,1),
            BLOCK1_TABLE11_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE11_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table12, dict(
            BLOCK1_TABLE12_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE12_TYPE=rd.randint(0,1),
            BLOCK1_TABLE12_ORDER=rd.randint(0,1),
            BLOCK1_TABLE12_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE12_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table13, dict(
            BLOCK1_TABLE13_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE13_TYPE=rd.randint(0,1),
            BLOCK1_TABLE13_ORDER=rd.randint(0,1),
            BLOCK1_TABLE13_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE13_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table14, dict(
            BLOCK1_TABLE14_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE14_TYPE=rd.randint(0,1),
            BLOCK1_TABLE14_ORDER=rd.randint(0,1),
            BLOCK1_TABLE14_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE14_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table15, dict(
            BLOCK1_TABLE15_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE15_TYPE=rd.randint(0,1),
            BLOCK1_TABLE15_ORDER=rd.randint(0,1),
            BLOCK1_TABLE15_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE15_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table16, dict(
            BLOCK1_TABLE16_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE16_TYPE=rd.randint(0,1),
            BLOCK1_TABLE16_ORDER=rd.randint(0,1),
            BLOCK1_TABLE16_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE16_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table17, dict(
            BLOCK1_TABLE17_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE17_TYPE=rd.randint(0,1),
            BLOCK1_TABLE17_ORDER=rd.randint(0,1),
            BLOCK1_TABLE17_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE17_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table18, dict(
            BLOCK1_TABLE18_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE18_TYPE=rd.randint(0,1),
            BLOCK1_TABLE18_ORDER=rd.randint(0,1),
            BLOCK1_TABLE18_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE18_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table19, dict(
            BLOCK1_TABLE19_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE19_TYPE=rd.randint(0,1),
            BLOCK1_TABLE19_ORDER=rd.randint(0,1),
            BLOCK1_TABLE19_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE19_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table20, dict(
            BLOCK1_TABLE20_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE20_TYPE=rd.randint(0,1),
            BLOCK1_TABLE20_ORDER=rd.randint(0,1),
            BLOCK1_TABLE20_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE20_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table21, dict(
            BLOCK1_TABLE21_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE21_TYPE=rd.randint(0,1),
            BLOCK1_TABLE21_ORDER=rd.randint(0,1),
            BLOCK1_TABLE21_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE21_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table22, dict(
            BLOCK1_TABLE22_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE22_TYPE=rd.randint(0,1),
            BLOCK1_TABLE22_ORDER=rd.randint(0,1),
            BLOCK1_TABLE22_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE22_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table23, dict(
            BLOCK1_TABLE23_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE23_TYPE=rd.randint(0,1),
            BLOCK1_TABLE23_ORDER=rd.randint(0,1),
            BLOCK1_TABLE23_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE23_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table24, dict(
            BLOCK1_TABLE24_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE24_TYPE=rd.randint(0,1),
            BLOCK1_TABLE24_ORDER=rd.randint(0,1),
            BLOCK1_TABLE24_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE24_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table25, dict(
            BLOCK1_TABLE25_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE25_TYPE=rd.randint(0,1),
            BLOCK1_TABLE25_ORDER=rd.randint(0,1),
            BLOCK1_TABLE25_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE25_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table26, dict(
            BLOCK1_TABLE26_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE26_TYPE=rd.randint(0,1),
            BLOCK1_TABLE26_ORDER=rd.randint(0,1),
            BLOCK1_TABLE26_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE26_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table27, dict(
            BLOCK1_TABLE27_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE27_TYPE=rd.randint(0,1),
            BLOCK1_TABLE27_ORDER=rd.randint(0,1),
            BLOCK1_TABLE27_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE27_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table28, dict(
            BLOCK1_TABLE28_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE28_TYPE=rd.randint(0,1),
            BLOCK1_TABLE28_ORDER=rd.randint(0,1),
            BLOCK1_TABLE28_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE28_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table29, dict(
            BLOCK1_TABLE29_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE29_TYPE=rd.randint(0,1),
            BLOCK1_TABLE29_ORDER=rd.randint(0,1),
            BLOCK1_TABLE29_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE29_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table30, dict(
            BLOCK1_TABLE30_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE30_TYPE=rd.randint(0,1),
            BLOCK1_TABLE30_ORDER=rd.randint(0,1),
            BLOCK1_TABLE30_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE30_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table31, dict(
            BLOCK1_TABLE31_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE31_TYPE=rd.randint(0,1),
            BLOCK1_TABLE31_ORDER=rd.randint(0,1),
            BLOCK1_TABLE31_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE31_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table32, dict(
            BLOCK1_TABLE32_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE32_TYPE=rd.randint(0,1),
            BLOCK1_TABLE32_ORDER=rd.randint(0,1),
            BLOCK1_TABLE32_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE32_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table33, dict(
            BLOCK1_TABLE33_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE33_TYPE=rd.randint(0,1),
            BLOCK1_TABLE33_ORDER=rd.randint(0,1),
            BLOCK1_TABLE33_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE33_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table34, dict(
            BLOCK1_TABLE34_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE34_TYPE=rd.randint(0,1),
            BLOCK1_TABLE34_ORDER=rd.randint(0,1),
            BLOCK1_TABLE34_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE34_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table35, dict(
            BLOCK1_TABLE35_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE35_TYPE=rd.randint(0,1),
            BLOCK1_TABLE35_ORDER=rd.randint(0,1),
            BLOCK1_TABLE35_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE35_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table36, dict(
            BLOCK1_TABLE36_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE36_TYPE=rd.randint(0,1),
            BLOCK1_TABLE36_ORDER=rd.randint(0,1),
            BLOCK1_TABLE36_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE36_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table37, dict(
            BLOCK1_TABLE37_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE37_TYPE=rd.randint(0,1),
            BLOCK1_TABLE37_ORDER=rd.randint(0,1),
            BLOCK1_TABLE37_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE37_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table38, dict(
            BLOCK1_TABLE38_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE38_TYPE=rd.randint(0,1),
            BLOCK1_TABLE38_ORDER=rd.randint(0,1),
            BLOCK1_TABLE38_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE38_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table39, dict(
            BLOCK1_TABLE39_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE39_TYPE=rd.randint(0,1),
            BLOCK1_TABLE39_ORDER=rd.randint(0,1),
            BLOCK1_TABLE39_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE39_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block1Table40, dict(
            BLOCK1_TABLE40_LOTTERY=rd.randint(1,20), 
            BLOCK1_TABLE40_TYPE=rd.randint(0,1),
            BLOCK1_TABLE40_ORDER=rd.randint(0,1),
            BLOCK1_TABLE40_SP_OPTION=rd.randint(0,1),
            BLOCK1_TABLE40_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.ZwischenteilIntro,

        yield pages.Zwischenteil1, dict(ZWISCHENFRAGE7 = 1, ),

        yield pages.Zwischenteil2, dict(ZWISCHENFRAGE4 = 1, ),

        yield pages.Zwischenteil3, dict(ZWISCHENFRAGE5 = 1, ),

        yield pages.Zwischenteil4, dict(ZWISCHENFRAGE9 = 1, ),

        yield pages.Zwischenteil5, dict(ZWISCHENFRAGE10 = 1, ),

        yield pages.Zwischenteil6, dict(ZWISCHENFRAGE12 = 1, ),

        yield pages.Zwischenteil7, dict(ZWISCHENFRAGE8 = 1, ),

        yield pages.Zwischenteil8, dict(ZWISCHENFRAGE15 = 1, ),

        yield pages.Zwischenteil9, dict(ZWISCHENFRAGE11 = 1, ),

        yield pages.Zwischenteil10, dict(ZWISCHENFRAGE13 = 1, ),

        yield pages.Zwischenteil11, dict(ZWISCHENFRAGE2 = 1, ),

        yield pages.Zwischenteil12, dict(ZWISCHENFRAGE16 = 1, ),

        yield pages.Zwischenteil13, dict(ZWISCHENFRAGE14 = 1, ),

        yield pages.Zwischenteil14, dict(ZWISCHENFRAGE1 = 1, ),

        yield pages.Zwischenteil15, dict(ZWISCHENFRAGE3 = 1, ),

        yield pages.Zwischenteil16, dict(ZWISCHENFRAGE6 = 1, ),

        yield pages.Block2Intro,

        yield pages.Block2Table1, dict(
            BLOCK2_TABLE1_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE1_TYPE=rd.randint(0,1),
            BLOCK2_TABLE1_ORDER=rd.randint(0,1),
            BLOCK2_TABLE1_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE1_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table2, dict(
            BLOCK2_TABLE2_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE2_TYPE=rd.randint(0,1),
            BLOCK2_TABLE2_ORDER=rd.randint(0,1),
            BLOCK2_TABLE2_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE2_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table3, dict(
            BLOCK2_TABLE3_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE3_TYPE=rd.randint(0,1),
            BLOCK2_TABLE3_ORDER=rd.randint(0,1),
            BLOCK2_TABLE3_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE3_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table4, dict(
            BLOCK2_TABLE4_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE4_TYPE=rd.randint(0,1),
            BLOCK2_TABLE4_ORDER=rd.randint(0,1),
            BLOCK2_TABLE4_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE4_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table5, dict(
            BLOCK2_TABLE5_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE5_TYPE=rd.randint(0,1),
            BLOCK2_TABLE5_ORDER=rd.randint(0,1),
            BLOCK2_TABLE5_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE5_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table6, dict(
            BLOCK2_TABLE6_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE6_TYPE=rd.randint(0,1),
            BLOCK2_TABLE6_ORDER=rd.randint(0,1),
            BLOCK2_TABLE6_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE6_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table7, dict(
            BLOCK2_TABLE7_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE7_TYPE=rd.randint(0,1),
            BLOCK2_TABLE7_ORDER=rd.randint(0,1),
            BLOCK2_TABLE7_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE7_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table8, dict(
            BLOCK2_TABLE8_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE8_TYPE=rd.randint(0,1),
            BLOCK2_TABLE8_ORDER=rd.randint(0,1),
            BLOCK2_TABLE8_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE8_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table9, dict(
            BLOCK2_TABLE9_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE9_TYPE=rd.randint(0,1),
            BLOCK2_TABLE9_ORDER=rd.randint(0,1),
            BLOCK2_TABLE9_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE9_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table10, dict(
            BLOCK2_TABLE10_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE10_TYPE=rd.randint(0,1),
            BLOCK2_TABLE10_ORDER=rd.randint(0,1),
            BLOCK2_TABLE10_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE10_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table11, dict(
            BLOCK2_TABLE11_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE11_TYPE=rd.randint(0,1),
            BLOCK2_TABLE11_ORDER=rd.randint(0,1),
            BLOCK2_TABLE11_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE11_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table12, dict(
            BLOCK2_TABLE12_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE12_TYPE=rd.randint(0,1),
            BLOCK2_TABLE12_ORDER=rd.randint(0,1),
            BLOCK2_TABLE12_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE12_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table13, dict(
            BLOCK2_TABLE13_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE13_TYPE=rd.randint(0,1),
            BLOCK2_TABLE13_ORDER=rd.randint(0,1),
            BLOCK2_TABLE13_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE13_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table14, dict(
            BLOCK2_TABLE14_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE14_TYPE=rd.randint(0,1),
            BLOCK2_TABLE14_ORDER=rd.randint(0,1),
            BLOCK2_TABLE14_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE14_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table15, dict(
            BLOCK2_TABLE15_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE15_TYPE=rd.randint(0,1),
            BLOCK2_TABLE15_ORDER=rd.randint(0,1),
            BLOCK2_TABLE15_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE15_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table16, dict(
            BLOCK2_TABLE16_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE16_TYPE=rd.randint(0,1),
            BLOCK2_TABLE16_ORDER=rd.randint(0,1),
            BLOCK2_TABLE16_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE16_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table17, dict(
            BLOCK2_TABLE17_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE17_TYPE=rd.randint(0,1),
            BLOCK2_TABLE17_ORDER=rd.randint(0,1),
            BLOCK2_TABLE17_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE17_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table18, dict(
            BLOCK2_TABLE18_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE18_TYPE=rd.randint(0,1),
            BLOCK2_TABLE18_ORDER=rd.randint(0,1),
            BLOCK2_TABLE18_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE18_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table19, dict(
            BLOCK2_TABLE19_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE19_TYPE=rd.randint(0,1),
            BLOCK2_TABLE19_ORDER=rd.randint(0,1),
            BLOCK2_TABLE19_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE19_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table20, dict(
            BLOCK2_TABLE20_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE20_TYPE=rd.randint(0,1),
            BLOCK2_TABLE20_ORDER=rd.randint(0,1),
            BLOCK2_TABLE20_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE20_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table21, dict(
            BLOCK2_TABLE21_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE21_TYPE=rd.randint(0,1),
            BLOCK2_TABLE21_ORDER=rd.randint(0,1),
            BLOCK2_TABLE21_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE21_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table22, dict(
            BLOCK2_TABLE22_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE22_TYPE=rd.randint(0,1),
            BLOCK2_TABLE22_ORDER=rd.randint(0,1),
            BLOCK2_TABLE22_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE22_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table23, dict(
            BLOCK2_TABLE23_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE23_TYPE=rd.randint(0,1),
            BLOCK2_TABLE23_ORDER=rd.randint(0,1),
            BLOCK2_TABLE23_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE23_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table24, dict(
            BLOCK2_TABLE24_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE24_TYPE=rd.randint(0,1),
            BLOCK2_TABLE24_ORDER=rd.randint(0,1),
            BLOCK2_TABLE24_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE24_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table25, dict(
            BLOCK2_TABLE25_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE25_TYPE=rd.randint(0,1),
            BLOCK2_TABLE25_ORDER=rd.randint(0,1),
            BLOCK2_TABLE25_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE25_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table26, dict(
            BLOCK2_TABLE26_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE26_TYPE=rd.randint(0,1),
            BLOCK2_TABLE26_ORDER=rd.randint(0,1),
            BLOCK2_TABLE26_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE26_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table27, dict(
            BLOCK2_TABLE27_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE27_TYPE=rd.randint(0,1),
            BLOCK2_TABLE27_ORDER=rd.randint(0,1),
            BLOCK2_TABLE27_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE27_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table28, dict(
            BLOCK2_TABLE28_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE28_TYPE=rd.randint(0,1),
            BLOCK2_TABLE28_ORDER=rd.randint(0,1),
            BLOCK2_TABLE28_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE28_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table29, dict(
            BLOCK2_TABLE29_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE29_TYPE=rd.randint(0,1),
            BLOCK2_TABLE29_ORDER=rd.randint(0,1),
            BLOCK2_TABLE29_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE29_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table30, dict(
            BLOCK2_TABLE30_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE30_TYPE=rd.randint(0,1),
            BLOCK2_TABLE30_ORDER=rd.randint(0,1),
            BLOCK2_TABLE30_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE30_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table31, dict(
            BLOCK2_TABLE31_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE31_TYPE=rd.randint(0,1),
            BLOCK2_TABLE31_ORDER=rd.randint(0,1),
            BLOCK2_TABLE31_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE31_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table32, dict(
            BLOCK2_TABLE32_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE32_TYPE=rd.randint(0,1),
            BLOCK2_TABLE32_ORDER=rd.randint(0,1),
            BLOCK2_TABLE32_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE32_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table33, dict(
            BLOCK2_TABLE33_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE33_TYPE=rd.randint(0,1),
            BLOCK2_TABLE33_ORDER=rd.randint(0,1),
            BLOCK2_TABLE33_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE33_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table34, dict(
            BLOCK2_TABLE34_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE34_TYPE=rd.randint(0,1),
            BLOCK2_TABLE34_ORDER=rd.randint(0,1),
            BLOCK2_TABLE34_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE34_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table35, dict(
            BLOCK2_TABLE35_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE35_TYPE=rd.randint(0,1),
            BLOCK2_TABLE35_ORDER=rd.randint(0,1),
            BLOCK2_TABLE35_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE35_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table36, dict(
            BLOCK2_TABLE36_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE36_TYPE=rd.randint(0,1),
            BLOCK2_TABLE36_ORDER=rd.randint(0,1),
            BLOCK2_TABLE36_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE36_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table37, dict(
            BLOCK2_TABLE37_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE37_TYPE=rd.randint(0,1),
            BLOCK2_TABLE37_ORDER=rd.randint(0,1),
            BLOCK2_TABLE37_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE37_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table38, dict(
            BLOCK2_TABLE38_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE38_TYPE=rd.randint(0,1),
            BLOCK2_TABLE38_ORDER=rd.randint(0,1),
            BLOCK2_TABLE38_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE38_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table39, dict(
            BLOCK2_TABLE39_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE39_TYPE=rd.randint(0,1),
            BLOCK2_TABLE39_ORDER=rd.randint(0,1),
            BLOCK2_TABLE39_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE39_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.Block2Table40, dict(
            BLOCK2_TABLE40_LOTTERY=rd.randint(1,20), 
            BLOCK2_TABLE40_TYPE=rd.randint(0,1),
            BLOCK2_TABLE40_ORDER=rd.randint(0,1),
            BLOCK2_TABLE40_SP_OPTION=rd.randint(0,1),
            BLOCK2_TABLE40_SP_DECISION=rd.randint(1, 21)
        ),

        yield pages.SetPayoff,
  
