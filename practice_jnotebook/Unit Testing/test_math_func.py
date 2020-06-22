from common_func import *
import pytest

def test_add():
    num1,num2 = 2,2
    result = add(num1,num2)
    assert result == 4
    
@pytest.mark.regression    
def test_sub():
    num1,num2 = 10,4
    result = sub(num1,num2)
    assert result == 6