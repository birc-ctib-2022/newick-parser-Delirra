"""Testing our Newick parser."""
from newick import parse

def test_me() -> None:
    """Test what you need to test."""
    tree = parse("(A, (B, C))")
    assert str(tree) == "(A,(B,C))"

    tree = parse("((A, B), C, ((D, E), F))")
    assert str(tree) == "((A,B),C,((D,E),F))"