import dogs,cats
import animal_functions

def test_get_oldest_animal_cat_and_dogs():
    dog1=dogs.Dog('Honey',2)
    dog2=dogs.Dog('Cody',12)
    dog3=dogs.Dog('Katie',12)
    dog4=dogs.Dog('Gracie',1)
    cat1=cats.Cat('Fonzi',15)

    assert 15 == animal_functions.get_oldest_animal(dog1,dog2,dog3,dog4,cat1),"The get_oldest_animal function did not return the oldest animal"

def test_get_oldest_animal_no_animals():
    assert 0 == animal_functions.get_oldest_animal(),"The get_oldest_animal function should return 0 if no animals passed in"

def test_get_oldest_animal_one_animal_float():
    dog1=dogs.Dog('Honey',2.1)


    assert 2.1 == animal_functions.get_oldest_animal(dog1),"The get_oldest_animal function had an issue with a float"

def test_get_oldest_animal_float_and_int():
    dog1=dogs.Dog('Honey',2.3)
    dog2=dogs.Dog('Cody',12)
    dog3=dogs.Dog('Katie',12.1)
    dog4=dogs.Dog('Gracie',1)
    cat1=cats.Cat('Fonzi',3.4)

    assert 12.1 == animal_functions.get_oldest_animal(dog1,dog2,dog3,dog4,cat1),"The get_oldest_animal function had an issue with mixed floats and integers"
