'''Pytest fixtures '''

import pytest

'''We use fixtures to avoid writing multiple db queries and breaking DRY rules'''

#create your pytest fixture
@pytest.fixture
def cursor():
    conn = db.connect("server")
    cur=conn.cursor()
    return cur


def test_johns_ID(cursor):
    id = cur.execute("select id from Employee WHERE name="John")
    assert id == 101
    
#----------Django example-----------#
    
@pytest.fixture(scope='session')
def mock_building():
    return Building.objects.create(
        name='bldg-name',
        code_1141='1234',
        company_name='company',
        address='address',
        post_code='P051 C0DE'
    )
    
def test_building_exists(mock_building):
    
    assert mock_building.name == 'mock-bldg' 

def test_building_in_listview(mock_building):
    
    assert mock_building.name.encode() in response.content
    
def test_str_method(mock_building):
    
    assert str(mock_building) == 'bldg-name'
    
#To see all fixtures:
#pytest --fixtures test_simplefactory.py (-v)
