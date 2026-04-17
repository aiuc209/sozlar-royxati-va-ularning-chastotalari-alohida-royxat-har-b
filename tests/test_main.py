import pytest

def soz_chastota(sozlar, chastotalar):
    natija = []
    for soz, chastota in zip(sozlar, chastotalar):
        natija.append(f"{soz}: {chastota}")
    return natija

def test_soz_chastota():
    sozlar = ["olma", "anor", "uzum"]
    chastotalar = [5, 3, 2]
    expected = ["olma: 5", "anor: 3", "uzum: 2"]
    assert soz_chastota(sozlar, chastotalar) == expected

def test_soz_chastota_empty():
    sozlar = []
    chastotalar = []
    expected = []
    assert soz_chastota(sozlar, chastotalar) == expected

def test_soz_chastota_unequal_length():
    sozlar = ["olma", "anor"]
    chastotalar = [5, 3, 2]
    with pytest.raises(ValueError):
        soz_chastota(sozlar, chastotalar)
