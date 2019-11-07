import pytest
from code import MyClass, Student


#assert "x" in/not in myvar / myvar.mymethod()

def test_add_and_lookup_entry():
    myvar = MyClass()
    myvar.add("name", 208)
    assert "name" in myvar.names()
    # assert "0208" in myvar.numbers()
    assert "randomstrings" not in myvar.numbers()
    assert type(123) == int
    

#Q what type are name and number and does it matter? if in the test i can add both int and strings what about in the function? do i define or is it ok?

# def test_credentials():
#     person = Student()
#     assert {person.name} in person.credentials()
#     print("test_credentials completed")

def test_func():
    result = "bla"
    assert "a" or "b" in result


