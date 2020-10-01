import random
from unittest import TestCase

from pokemon_symbols import pokemon_get_symbol, pokemon_last_symbol


class TestPokemonGetSymbol(TestCase):
    def setUp(self):
        try:
            pokemon_get_symbol("00:0000")
        except NotImplementedError:
            raise self.skipTest("Exercise not started")
        except Exception:
            pass

    def test_get_symbol(self):
        self.assertEqual("LoadTitleMonSprite", pokemon_get_symbol("01:4524"))

    def test_no_symbol(self):
        self.assertIsNone(pokemon_get_symbol("03:5000"))

    def test_two_symbols(self):
        self.assertEqual(
            "PokecenterWarpTileIDs", pokemon_get_symbol("03:4503")
        )

    def test_performance(self):
        for _ in range(1000):
            bank, offset = divmod(random.randint(0, 0xffff), 0x4000)
            offset += 0x4000 * (bank > 0)
            address = f"{bank:02x}:{offset:04x}"
            pokemon_get_symbol(address)


class TestPokemonLastSymbol(TestCase):
    def setUp(self):
        try:
            pokemon_last_symbol("00:0000")
        except NotImplementedError:
            raise self.skipTest("Exercise not started")
        except Exception:
            pass

    def test_same_symbol(self):
        self.assertEqual(
            "Music_SafariZone_Ch1", pokemon_last_symbol("02:7c2e")
        )
        self.assertEqual(
            "Music_SafariZone_Ch1", pokemon_last_symbol("02:7c40")
        )
        self.assertEqual("WildDataPointers", pokemon_last_symbol("03:5000"))

    def test_no_symbol(self):
        self.assertIsNone(pokemon_last_symbol("00:0040"))

    def test_two_symbols(self):
        self.assertEqual(
            "PokecenterWarpTileIDs", pokemon_last_symbol("03:4504")
        )

    def test_performance(self):
        for _ in range(1000):
            bank, offset = divmod(random.randint(0, 0xffff), 0x4000)
            offset += 0x4000 * (bank > 0)
            address = f"{bank:02x}:{offset:04x}"
            pokemon_last_symbol(address)
