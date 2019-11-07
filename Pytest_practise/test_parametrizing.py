import pytest

@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
    print("test_eval works") #to display this message add -s to your pytest command

@pytest.mark.parametrize("myvar1, myvar2", [("2", 2), ("2",2)])
def test_mymethod1(myvar1, myvar2):
    assert eval(myvar1) == myvar2
    print("test mymethod2 works")

@pytest.mark.parametrize("myvar1, myvar2", [(2, 2), (2,2)])
def test_mymethod2(myvar1, myvar2):
    assert myvar1 == myvar2
    print("test 3 works")

@pytest.mark.parametrize("myvar1, myvar2", [(2, 2), (2,2)])
def test_mymethod2(myvar1, myvar2):
    assert myvar1 == myvar2
    print("test mymethod2 works")

@pytest.mark.parametrize("myvar1, myvar2", [("stringa", "stringb"), ("stringa","stringb")])
def test_mymethod3(myvar1, myvar2):
    assert myvar1 == "stringa" or "stringb"
    print("test mymethod3 works")    

#In cases where you have a bug or functionality to be fixed you can write a test and ALLOW/EXPECT it to fail (sthing to fix later)
# in pytest this is called an expected fail or xfail 

@pytest.mark.parametrize("myvar1, myvar2", [("crisps", "crisps"), pytest.param("drinks","drinks",marks=pytest.mark.xfail)])
def test_Expectedfailfordrinks(myvar1, myvar2):
    assert myvar1 == "crisps"
    print("test xfail (expected fail) test works")  


# @pytest.mark.parametrize("iscircuit", [(4,4)])
# def test_greaterlessthan(iscircuit):
#     mylist="haha"
#     iscircuit = len(mylist)
#     assert len(iscircuit) == 4
#     print("test greater less than")

def myfunction(x):
    return x

#--------------FIXTURES-------------#


@pytest.fixture()
def testCase(request):
    testCase = {"input": 8,
    "expectedresult": 8}
    return testCase

def test_my_function(testCase):
    result = myfunction(testCase["input"])
    assert result == testCase["expectedresult"]