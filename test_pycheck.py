import pytest
from check import checking


class Testing():
    def test_presence(self):
        assert checking("./remi.sh") == True
    
    def test_absence(self):
        assert checking("sue.sh") == False


#this is the main area
if __name__ == '__main__':
    pytest.main