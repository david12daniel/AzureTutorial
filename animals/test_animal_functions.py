import dogs,cats
import animal_functions

dog1=dogs.Dog('Honey',2)
dog2=dogs.Dog('Cody',12)
dog3=dogs.Dog('Katie',12)
dog4=dogs.Dog('Gracie',1)
cat1=cats.Cat('Fonzi',15)

assert 15 == animal_functions.get_oldest_animal(dog1,dog2,dog3,dog4,cat1)
