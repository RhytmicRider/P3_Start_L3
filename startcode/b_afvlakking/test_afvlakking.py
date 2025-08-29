from afvlakking import aantal_vakjes

def test_vpw_testgevallen():
    assert aantal_vakjes([1, 2]) == 0      # testgeval 1
    assert aantal_vakjes([2, 1]) == 1      # testgeval 2
    assert aantal_vakjes([5, 4, 3, 2, 1]) == 10  # testgeval 3

def test_vb1_geen_afvlakking_nodig():
    assert aantal_vakjes([1, 2]) == 0

def test_vb2_één_blokje_bij():
    assert aantal_vakjes([2, 1]) == 1

def test_vb3_grote_daling():
    assert aantal_vakjes([5, 4, 3, 2, 1]) == 10

def test_complexe_case():
    assert aantal_vakjes([1, 4, 3, 2, 5, 3, 6, 5]) == 6

def test_al_gelijkblijvend():
    assert aantal_vakjes([3, 3, 3, 3]) == 0

def test_oplopend():
    assert aantal_vakjes([1, 2, 3, 4]) == 0

def test_random_dalingen():
    assert aantal_vakjes([3, 1, 4, 2, 5]) == 4

