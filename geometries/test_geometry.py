import circle
import rectangle
import math

def test_circle_0():
    circ=circle.Circle(0.0)
    area = circ.area()
    perimeter = circ.perimeter()
    assert 0.0 == area and 0.0 == perimeter

def test_circle_10():
    circ=circle.Circle(10.0)
    area = circ.area()
    perimeter = circ.perimeter()
    assert math.pi*10.0*10.0 == area and 2*math.pi*10.0 == perimeter

def test_rectangle_0_10():
    rect=rectangle.Rectangle(0.0,10.0)
    area = rect.area()
    perimeter = rect.perimeter()
    assert 0.0 == area and 0.0 == perimeter

def test_rectangle_10_10():
    rect=rectangle.Rectangle(10.0,10.0)
    area = rect.area()
    perimeter = rect.perimeter()
    assert 100.0 == area and 40.0 == perimeter

def test_rectangle_20_10():
    rect=rectangle.Rectangle(20.0,10.0)
    area = rect.area()
    perimeter = rect.perimeter()
    assert 200.0 == area and 60.0 == perimeter

def test_rectangle_10_20():
    rect=rectangle.Rectangle(10.0,20.0)
    area = rect.area()
    perimeter = rect.perimeter()
    assert 200.0 == area and 60.0 == perimeter