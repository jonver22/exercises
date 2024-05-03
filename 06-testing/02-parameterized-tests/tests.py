from parentheses import matching_parentheses


def test_matching_parentheses():
    assert matching_parentheses('()')
    assert matching_parentheses('')
    assert matching_parentheses('(())')
    assert not matching_parentheses('(()')
    assert not matching_parentheses(')(')