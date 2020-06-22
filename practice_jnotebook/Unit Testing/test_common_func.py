from common_func import linear_search
import pytest

def test_key_present_ls():
    lst = [1,2,3,4,5,6]
    key = 4
    result = linear_search(lst,key)
    assert result == True
    
@pytest.mark.regression    
def test_key_not_present_ls():
    lst = [1,2,3,4,5]
    key = 10
    result = linear_search(lst,key)
    assert result == False