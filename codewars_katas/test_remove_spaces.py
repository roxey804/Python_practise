# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 15:20:19 2019

@author: rnikoo
"""
import pytest

@pytest.fixture 
def remove_spaces():
    x = "ab ac us"  
    nospace = x.replace(" ","")
    return nospace

def test_remove_spaces(remove_spaces):
    assert 1 == 1
    assert "a" in nospace
    
