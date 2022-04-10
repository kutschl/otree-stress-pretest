from . import pages
from ._builtin import Bot
from .models import Constants

import random as rd


def getVorname():
    Vornamen = ["Lucy", "Ella", "Amy", "Emely", "Finja", "Amelie", "Luise", "Frieda", "Katharina", "Romy", "Juna", "Theresa", "Eva", "Julia", "Anna", "Carla", "Paulina", "Elisabeth", "Rosa", "Mia", "Maya", "Selma", "Edda", "Flora", "Berenike", "Simone", "Elena", "Meike", "Susanne", "Annika", "Augusta", "Alba", "Wilma", "Annegret", "Aglaia", "Aaliyah", "Annabelle", "Alma", "Alicia", "Anette", "Astrid", "Anisha", "Antke", "Abigail", "Aideen", "Aini", "Aida", "Aamenah", "Ariane", "Adriana", "Alexandra", "Ava", "Arielle", "Allissa", "Aamu", "Arzu", "Anouk", "Andrea", "Bianca", "Blanka", "Benita", "Bettina", "Bamika", "Bente", "Barbara", "Berit", "Bentje", "Birte", "Brigitte", "Christiane", "Charlotte", "Catherina", "Caroline", "Caren", "Caecilia", "Celine", "Coco", "Chaya", "Dalia", "Deenah", "Daphne", "Delia", "Dari", "Doerte", "Djamila", "Dominique", "Doerte", "Dorothee", "Emira", "Emily", "Elif", "Ellen", "Enna", "Ebba", "Eleni", "Freya", "Fiona", "Franziska", "Luzia", "Fabienne", "Mädchen", "Fiona", "Felina", "Felicitas", "Fabia", "Fabiola", "Fabrizia", "Filomae", "Floris", "Fae", "Fanny", "Fritzi", "Greta", "Gabrielle", "Grit", "Gwen", "Gabi", "Gila", "Giorgina", "Gisele", "Heike", "Hanna", "Helena", "Haima", "Heike", "Helen", "Isabell", "Ida", "Ilona", "Ingrid", "Iris", "Ira", "Iara", "Ivette", "Irma", "Jardis", "Juni", "Juna", "Josephine", "Jella", "Jill", "Jennifer", "Jakobine", "Jessika", "Julie", "Jasmin", "Joana", "Jaqueline", "Jonna", "Jean", "Janis", "Jodi", "Jen", "Justyna", "Jutta", "Kathleen", "Kayra", "Klara", "Kiara", "Kathrin", "Catrin", "Kiki", "Judith", "Celia", "Kaaria", "Kerstin", "Kim", "Kader", "Kaisa", "Liv", "Livia", "Louisa", "Lucy", "Lina", "Lena", "Leonie", "Lea", "Leni", "Lotta", "Laura", "Lara", "Lia", "Lisa", "Luna", "Linda", "Laureen", "Liv", "Liz", "Mona", "Mareen", "Mathilda", "Marlene", "Marianne", "Mara", "Mina", "Magdalena", "Miriam", "Marianne", "Martje", "Maeve", "Mae", "Mädchen", "Nadja", "Nadine", "Nele", "Nora", "Nina", "Nada", "Nadeshda", "Nancy", "Nova", "Nika", "Nike", "Oda", "Odilie", "Okka", "Olea", "Odett", "Olivia", "Odilia", "Oana", "Pia", "Paula", "Phlomena", "Paloma", "Paris", "Paola", "Poppy", "Panja", "Pardis", "Quirine", "Quinta", "Qara", "Ria", "Rita", "Raina", "Rabea", "Radost", "Rabi", "Ronina", "Rae", "Radia", "Svea", "Smila", "Sofia", "Sonja", "Sophie", "Stella", "Sarah", "Silvie", "Silke", "Sila", "Siri", "Sarah", "Saara", "Svenja", "Sabine", "Sandra", "Tiffanie", "Thea", "Tilda", "Tardis", "Tamina", "Tamy", "Trudi", "Tea", "Tima", "Tabia", "Tassja", "Tilla", "Tabita", "Tahua", "Uli", "Ulrike", "Ute", "Uda", "Ulla", "Ulrika", "Ulva", "Ulvi", "Uma", "Violeta", "Victoria", "Vanessa", "Valentine", "Valeska", "Wandy", "Waris", "Walli", "Waltraud", "Wanda", "Xenia", "Xani", "Xanthe", "Yvonne", "Yu", "Yla", "Zoe", "Zilla", "Zuri", "Zamira", "Lukas", "Konstantin", "Ben", "Jonas", "Elias", "Niklas", "David", "Oskar", "Philipp", "Leon", "Noah", "Luis", "Paul", "Finn", "Felix", "Julian", "Maximilian", "Henry", "Tim", "Karl", "Friedrich", "Peter", "Quirin", "Liam", "Linus", "Quentin", "Paul", "Johannes", "Alexander", "Anton", "Aras", "Asis", "Adrian", "Arthur", "Adam", "Arian", "Amos", "Arik", "Ake", "Altfried", "Ari", "Andreas", "Allessandro", "Achim", "Ben", "Bela", "Baldur", "Benedikt", "Beat", "Bernd", "Bertram", "Blue", "Badi", "Batiste", "Bastian", "Caleb", "Caspar", "Calvin", "Cadmus", "Christoph", "Cedrik", "Camern", "Carsten", "Cainan", "Cem", "Carl", "Cyranus", "Curt", "Daniel", "Dominik", "Darius", "Dario", "Dag", "Diminic", "Damian", "Diego", "Dieter", "Demian", "Dewis", "Dirk", "Donald", "Enzo", "Emil", "Erik", "Edwin", "Eliah", "Ethan", "Erwin", "Eliot", "Enes", "Emilio", "Ebbo", "Eberhard", "Edgar", "Fabrizius", "Finn", "Fabian", "Fabio", "Finjas", "Franz", "Jungen", "Falko", "Fatih", "Fynn", "Flavio", "Fady", "Fritz", "Falko", "Gabriel", "Gustav", "Guiseppe", "Günter", "Gerhard", "Georg", "Gel", "Gerald", "Geoffrey", "Gismund", "Giulio", "Godo", "Henri", "Hannes", "Henry", "Henrik", "Hendrik", "Heiko", "Haku", "Hanno", "Hugo", "Henryk", "Hardy", "Hagar", "Hafiz", "Haile", "Hakan", "Hasso", "Harry", "Hauke", "Harun", "Hayo", "Idil", "Ian", "Izzy", "Ibrahim", "Igor", "Jack", "Jules", "Julian", "Jan", "Jakob", "Jaap", "Jonathan", "Jannik", "Jona", "Jannis", "Joel", "Jonte", "Jarin", "Jörn", "Jari", "Jannik", "Jukka", "Samo", "Jaakov", "Jeremy", "Jarne", "Kilian", "Kai", "Kylan", "Kristian", "Kasper", "Kadmos", "Klaus", "Kaarle", "Kevin", "Kadir", "Konrad", "Lukas", "Leon", "Leopold", "Luca", "Linas", "Roland", "Leo", "Lennard", "Luke", "Lenny", "Lasse", "Lion", "Luca", "Lutz", "Levi", "Matthias", "Moritz", "Meteo", "Mats", "Matthis", "Mattes", "Milo", "Mika", "Maxim", "Jungen", "Marlon", "Mark", "Matti", "Martin", "Morris", "Miran", "Miro", "Niklas", "Nika", "Niko", "Nabil", "Noel", "Nils", "Nick", "Neo", "Nadeem", "Namo", "Nepomuk", "Oscar", "Ole", "Oliver", "Olivier", "Onur", "Owen", "Obbo", "Idil", "Otto", "Oswald", "Paul", "Phil", "Patrick", "Paavo", "Pamir", "Pascal", "Peter", "Quinn", "Quazim", "Kasimir", "René", "Riko", "Robin", "Raphael", "Rudi", "Remigius", "Richard", "Radi", "Rainer", "Rasmus", "Ruben", "Samuel", "Stefan", "Sascha", "Serkan", "Marco", "Manuel", "Tom", "Tim", "Theo", "Theodor", "Thilo", "Till", "Timo", "Tino", "Tiny", "Taylor", "Titus", "Tristan", "Tizian", "Todd", "Thomas", "Taavi", "Tillmann", "Uwe", "Udo", "Ugor", "Ulrich", "Uli", "Ulas", "Ulf", "Volker", "Vinzent", "Valentin", "Vitus", "Volker", "Valentin", "Vidu", "Valerio", "Wilhelm", "William", "Will", "Walter", "Wanja", "Wadi", "Walid", "Xaver", "Yannis", "Yannik", "Yoshi", "Yunus"]
    return Vornamen[rd.randint(0, len(Vornamen)-1)]


def getNachname():
    Nachnamen = ["Müller/Mueller", "Schmidt", "Schneider", "Fischer", "Meyer", "Weber", "Hofmann", "Wagner", "Becker", "Schulz", "Schäfer/ Schaefer", "Koch", "Bauer", "Richter", "Klein", "Schröder/ Schroeder", "Wolf", "Neumann", "Schwarz", "Schmitz", "Krüger/ Krueger", "Braun", "Zimmermann", "Schmitt", "Lange", "Hartmann", "Hofmann", "Krause", "Werner", "Meier", "Schmid", "Schulze", "Lehmann", "Köhler/ Koehler", "Maier", "Hermann", "König/ Koenig", "Mayer", "Walter", "Peters", "Möller/ Moeller", "Huber", "Kaiser", "Fuchs", "Scholz", "Weiss/ Weiß", "Lang", "Jung", "Hahn", "Keller", "Vogel", "Friedrich", "Günther", "Schubert", "Berger", "Frank", "Roth", "Beck", "Winkler", "Lorenz", "Baumann", "Albrecht", "Ludwig", "Franke", "Simon", "Böhm", "Schuster", "Schuhmacher", "Kraus", "Winter", "Otto", "Krämer", "Stein", "Vogt", "Martin", "Jäger", "Groß", "Sommer", "Brandt", "Haas", "Heinrich", "Seidel", "Schreiber", "Schulte", "Graf", "Dietrich", "Ziegler", "Engel", "Kühn", "Kuhn", "Pohl", "Horn", "Thomas", "Busch", "Wolff", "Sauer", "Bergmann", "Pfeffer", "Voigt", "Ernst"]
    return Nachnamen[rd.randint(0, len(Nachnamen)-1)]


def getStrasse():
    Hausnummer = rd.choice([rd.randint(1, 25), rd.randint(1, 50), rd.randint(1, 100)])
    Strasse = f'{getNachname()}{rd.choice([str("strasse"), str("straße"), str("weg"), str("allee"), str("chausse"), str("gasse")])}'
    return f'{Strasse} {Hausnummer}'


def getPLZ():
    return f'{rd.randint(0,9)}{rd.randint(0,9)}{rd.randint(0,9)}{rd.randint(0,9)}{rd.randint(0,9)}'


def getStadt():
    Staedte = ["Aachen", "Aalen", "Amberg", "Annaberg-Buchholz", "Ansbach", "Aschaffenburg", "Auerbach/Vogtland", "Augsburg", "Bad Kreuznach", "Baden-Baden", "Bamberg", "Baunatal", "Bautzen", "Bayreuth", "Berlin", "Bernau bei Berlin", "Biberach an der Riß", "Bielefeld", "Bocholt", "Bochum", "Bonn", "Bottrop", "Brandenburg an der Havel", "Braunschweig", "Bremen", "Bremerhaven", "Castrop-Rauxel", "Celle", "Chemnitz", "Coburg", "Cottbus", "Darmstadt", "Delitzsch", "Delmenhorst", "Dessau-Roßlau", "Dortmund", "Dresden", "Duisburg", "Düren", "Düsseldorf", "Eberswalde", "Eisenach", "Eisenhüttenstadt", "Emden", "Erfurt", "Erkner", "Erlangen", "Essen", "Esslingen am Neckar", "Falkensee", "Flensburg", "Forst (Lausitz)", "Frankenthal (Pfalz)", "Frankfurt (Oder)", "Frankfurt am Main", "Freiberg", "Freiburg im Breisgau", "Friedrichshafen", "Fulda", "Fürth", "Gelsenkirchen", "Gera", "Gießen", "Gladbeck", "Glauchau", "Goslar", "Gotha", "Greifswald", "Gräfelfing", "Göttingen", "Gütersloh", "Hagen", "Halberstadt", "Halle (Saale)", "Hamburg", "Hameln", "Hamm", "Hanau", "Hannover", "Heidelberg", "Heidenheim an der Brenz", "Heilbronn", "Hennigsdorf", "Herford", "Herne", "Hildesheim", "Hof", "Hoyerswerda", "Ingolstadt", "Iserlohn", "Jena", "Kaiserslautern", "Kamenz", "Karlsruhe", "Kassel", "Kaufbeuren", "Kempten (Allgäu)", "Kiel", "Koblenz", "Konstanz", "Krefeld", "Köln", "Landau in der Pfalz", "Landsberg am Lech", "Landshut", "Leipzig", "Leverkusen", "Limbach-Oberfrohna", "Lindau (Bodensee)", "Ludwigsburg", "Ludwigshafen am Rhein", "Lörrach", "Lübeck", "Lüneburg", "Magdeburg", "Mainz", "Mannheim", "Marburg", "Memmingen", "Mönchengladbach", "Mühlhausen/Thüringen", "Mülheim an der Ruhr", "München", "Münster", "Neu-Ulm", "Neubrandenburg", "Neuenhagen bei Berlin", "Neumünster", "Neuruppin", "Neuss", "Neustadt am Rübenberge", "Neustadt an der Weinstraße", "Neustadt bei Coburg", "Neuwied", "Nordhausen", "Nürnberg", "Oberhausen", "Offenbach am Main", "Offenburg", "Oldenburg", "Oranienburg", "Osnabrück", "Passau", "Pforzheim", "Pirmasens", "Pirna", "Plauen", "Potsdam", "Quedlinburg", "Recklinghausen", "Regensburg", "Remscheid", "Reutlingen", "Riesa", "Rosenheim", "Rostock", "Saarbrücken", "Salzgitter", "Sassnitz", "Schwabach", "Schwedt/Oder", "Schweinfurt", "Schwerin", "Schwäbisch Gmünd", "Siegen", "Sindelfingen", "Solingen", "Speyer", "Stendal", "Straubing", "Stuttgart", "Suhl", "Taucha", "Teltow", "Teterow", "Trier", "Tübingen", "Ulm", "Velten", "Viersen", "Villingen-Schwenningen", "Weiden in der Oberpfalz", "Weimar", "Wiesbaden", "Wilhelmshaven", "Wismar", "Witten", "Wittenberg", "Wolfsburg", "Wolgast", "Worms", "Wuppertal", "Würzburg", "Zweibrücken", "Zwickau"]
    return Staedte[rd.randint(0, len(Staedte)-1)]


def getEmail():
    Email_prefix = f'{getVorname()}.{getNachname()}.{getPLZ()}'
    Email_suffix = 'mail.de'
    return f'{Email_prefix}@{Email_suffix}'


def getIBAN():
    IBAN = ["DE02120300000000202051", "DE02500105170137075030", "DE02100500000054540402", "DE02300209000106531065", "DE02200505501015871393", "DE02100100100006820101", "DE02300606010002474689", "DE02600501010002034304", "DE02700202700010108669", "DE02700100800030876808", "DE02370502990000684712", "DE88100900001234567892", "DE02701500000000594937", "AT026000000001349870", "AT021420020010147558", "AT023200000000641605", "AT021200000703447144", "AT022011100003429660", "AT022081500000698597", "AT022040400040102634", "AT023400000002613800", "AT022032032102118431", "AT023500000001070671", "AT021860000012387890", "AT023600000000679514", "AT021700000432040976", "AT022050303300646365", "AT023225000000704957", "CH0209000000100013997", "CH0204835000626882001", "CH0200700110000387896", "CH0208401000051138778", "CH0200767000C51001987", "CH020024024014511740P", "CH0200790016271403331", "CH0200781125534343504", "CH020023023012625140U", "CH0200769016143198123", "CH2200784102000123454", "CH0206300016120442405", "CH0200761016090504437", "CH0200778010152237210", "CH9305881020624751001", "LI0208800000017197386", "LI0208805502400560249", "LI02088100000191010AC", "LI0308803103143000000", "LI0508812105028570001", "LI0608808000220182703", "LI15088110605699K002E", "LI0608813201408880001", "LI2608802001003488101", "LI5708801200185100814"]
    return IBAN[rd.randint(0, len(IBAN)-1)]


def getBIC():
    BIC = ["BYLADEM1001", "INGDDEFF", "BELADEBE", "CMCIDEDD", "HASPDEHH", "PBNKDEFF", "DAAEDEDD", "SOLADEST600", "HYVEDEMM", "PBNKDEFF", "COKSDE33", "BEVODEBB", "SSKMDEMM", "OPSKATWW", "EASYATW1", "RLNWATWW", "BKAUATWW", "GIBAATWW", "STSPAT2G", "SBGSAT2S", "RZOOAT2L", "ASPKAT2L", "RVSAAT2S", "VKBLAT2L", "RZTIAT22", "BFKKAT2K", "SPIHAT22", "RLNWATWWGTD", "POFICHBE", "CRESCHZZ80A", "ZKBKCHZZ80A", "MIGRCHZZ", "BCVLCH2L", "UBSWCHZH12A", "KBBECH22", "KBSGCH22", "UBSWCHZH80A", "KBTGCH22", "VABECH22", "KBAGCH22", "LUKBCH2260A", "AHHBCH22", "LILALI2X", "VPBVLI2X", "BLFLLI2X", "HYIBLI22", "VOAGLI22", "CBKVLI2X", "BFRILI22", "RAIBLI22", "NBANLI22", "BALPLI22"]
    return BIC[rd.randint(0, len(BIC)-1)]


class PlayerBot(Bot):

    def play_round(self):
        yield pages.Willkommen,
        yield pages.Einverstaendniserklaerung, dict(
            ACCEPT=True,
        )
        yield pages.Anmeldung, dict(
            VORNAME=getVorname(),
            NACHNAME=getNachname(),
            STRASSE=getStrasse(),
            PLZ=getPLZ(),
            STADT=getStadt(),
            EMAIL=getEmail(),
            IBAN=getIBAN(),
            BIC=getBIC()
        )
