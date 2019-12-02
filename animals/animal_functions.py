
def get_oldest_animal(*args):
    max_age=0
    for i in args:
        if i.age > max_age:
            max_age=i.age

    return max_age