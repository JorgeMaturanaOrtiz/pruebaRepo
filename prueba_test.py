import pytest
import prueba

#-----------------------
@pytest.mark.fne
@pytest.mark.parametrize('a, b, c',
                         [(2,2,4),(0,0,0),(-3,1,-2)])
def test_prueba_fne(a, b, c):
    assert prueba.suma(a, b) == c
    
#-----------------------
@pytest.mark.fae
@pytest.mark.parametrize('a, b, c',
                         [('a',0,TypeError),('a','b','ab')])
def test_prueba_fae(a, b, c):
    assert prueba.suma(a, b) == c
