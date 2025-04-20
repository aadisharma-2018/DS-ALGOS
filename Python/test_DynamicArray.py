from DynamicArray import DynamicArray

def test_pushback_and_get():
    arr = DynamicArray(2)
    arr.pushback(10)
    arr.pushback(20)
    assert arr.get(0) == 10
    assert arr.get(1) == 20

def test_resize():
    arr = DynamicArray(1)
    arr.pushback(1)
    arr.pushback(2)  
    assert arr.getCapacity() == 2
    assert arr.get(1) == 2

def test_set():
    arr = DynamicArray(3)
    arr.pushback(5)
    arr.set(0, 10)
    assert arr.get(0) == 10

def test_popback():
    arr = DynamicArray(2)
    arr.pushback(100)
    arr.pushback(200)
    last = arr.popback()
    assert last == 200
    assert arr.getSize() == 1

def test_getSize_and_getCapacity():
    arr = DynamicArray(4)
    arr.pushback(1)
    arr.pushback(2)
    assert arr.getSize() == 2
    assert arr.getCapacity() == 4