from binary_search import binary_search

def test_binary_search():
    assert binary_search([1, 2, 3], 3) == 2
    assert binary_search([1, 2, 3], 1) == 0
