import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        # Muotoa: Nimi, joukkue, maalit, syötöt
        # Pisteet = maalit + syötöt
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_hae_pelaaja(self):
        # Testataan, että olemassa oleva pelaaja löytyy
        pelaaja = self.stats.search("Semenko")
        self.assertEqual(pelaaja.name, "Semenko")

    def test_hae_pelaaja_jota_ei_ole(self):
        # Testataan, että pelaajaa jota ei ole olemassa ei löydy
        pelaaja = self.stats.search("ErkkiEsimerkki")
        self.assertIsNone(pelaaja)

    def test_hae_joukkueen_pelaajat(self):
        # Testataan, että joukkueen pelaajat löytyvät
        pelaajat = self.stats.team("EDM")
        self.assertEqual(len(pelaajat), 3)

    def test_hae_parhaat_pelaajat(self):
        # Testataan, että parhaat pelaajat löytyvät
        pelaajat = self.stats.top(2)
        self.assertEqual(len(pelaajat), 2)
        self.assertEqual(pelaajat[0].name, "Gretzky")
        self.assertEqual(pelaajat[1].name, "Lemieux")


