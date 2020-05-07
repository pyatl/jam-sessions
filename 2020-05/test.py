import unittest

import Start


class TestEasy(unittest.TestCase):
    def test_average(self):
        self.assertEqual(Start.Easy("1Easy.csv"), 1238)


class TestMedium(unittest.TestCase):
    def test_list_int(self):
        """
        Test 2Medium
        """
        completion_list = ['CATHERIN', 'TOM', '', 'Luke Shoun',
                           'Marquitta Strassel'
            , 'BEBE', 'CARRION', '', 'Lynn Gartman', 'Isis Ade'
            , 'WILLENA', 'PERRIN', '', 'Valentin Puthoff', 'Jung Imrie'
            , 'DIA', 'HORAN', '', 'Florentino Lohwasser', 'Kevin Himebaugh'
            , 'DENISSE', 'HALES', '', 'Jamison Discenza', 'Edna Rippon'
            , 'DELORAS', 'GARMON', '', 'Kirby Garringer', 'Tiesha Fannings'
            , 'DELILA,FITTS', '', 'Theodore Mccament', 'Charis Lauster'
            , 'DAYSI', 'DELL', '', 'Jeffry Raymo', 'Megan Hogancamp'
            , 'DAKOTA', 'BOHN', '', 'Maynard Kefauver', 'Desiree Centola'
            , 'CURTIS', 'ATCHISON', '', 'Mary Bollozos', 'Shana Mould'
            , 'CRYSTLE', 'WORTH', '', 'Adolfo Gasco', 'Curtis Dukelow'
            , 'CONCHA', 'WISNIEWSKI', '', 'Nicholas Dado', 'Esta Holla'
            , 'COLBY', 'WILL', '', 'Virgilio Ranft', 'Laurence Cina'
            , 'CLARETTA', 'VANWINKLE', '', 'Wayne Champoux', 'Karon Adkins'
            , 'CHU', 'STURM', '', 'Julio Rio', 'Krystina Koszyk'
            , 'CHRISTIA', 'SALLEE', '', 'Jonathon Suganuma', 'Debbra Berky'
            , 'CHARLSIE', 'PROSSER', '', 'Josue Carasco', 'Dean Buchta'
            , '', 'FAWCETT', '', 'Michal Woodside', 'Coral Solon'
            , '', 'EADS', '', 'Martin Farson', 'Estell Nanney'
            , '', 'DRIGGERS', '', 'Rashad Pistoresi', 'Margot Rosenberg'
            , '', 'DONLEY', '', 'Randal Homs', 'Vicky Mendonsa'
            , '', 'COLLETT', '', 'Olin Trafton', 'Veola Espenoza']
        self.assertListEqual(Start.Medium("2Medium.csv"), completion_list)


class TestHard(unittest.TestCase):
    def test_list_goods(self):
        """
        Test the Hard Case
        """
        product_list = ["5.2 in Midas 2-in-1 Classic Fragrance Warmer", 17.99,
                        "600 Thread Count Supima Cotton Sateen Sheet Set",
                        69.97 - 84.97,
                        "StyleWell Glenville White Kitchen Cart with 2 Drawers",
                        183.20,
                        "4 in. x 16.74 in. 16-Piece Distressed Barn Wood Plank Blue Peel and Stick Wall Decals",
                        20.24,
                        "Cuckoo 6-Cup Induction Heating Pressure Rice Cooker in Dark Gray",
                        520.00, ]
        self.assertListEqual(Start.Hard("3Hard.csv"), product_list)
