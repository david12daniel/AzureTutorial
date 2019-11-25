class Node:
    def __init__(self,id):
        self.id=id
        self.right=None
        self.left=None
    def find_max_id(self):
        if self.right is not None and self.left is not None:
            if (self.right.find_max_id() > self.left.find_max_id()):
                if (self.right.find_max_id() > self.id):
                    print(f"ID: {self.id}  returning {self.right.find_max_id()}")
                    return self.right.find_max_id()
                else:
                    print(f"ID: {self.id}  returning {self.id}")
                    return self.id
            else:
                if (self.left.find_max_id() > self.id):
                    print(f"ID: {self.id}  returning {self.left.find_max_id()}")
                    return self.left.find_max_id()
                else:
                    print(f"ID: {self.id}  returning {self.id}")
                    return self.id
        elif self.left is not None:
            if (self.left.find_max_id() > self.id):
                print(f"ID: {self.id}  returning {self.left.find_max_id()}")
                return self.left.find_max_id()
            else:
                print(f"ID: {self.id}  returning {self.id}")
                return self.id
        elif self.right is not None:
            if (self.right.find_max_id() > self.id):
                print(f"ID: {self.id}  returning {self.right.find_max_id()}")
                return self.right.find_max_id()
            else:
                print(f"ID: {self.id}  returning {self.id}")
                return self.id
        else:
            print(f"ID: {self.id}  returning {self.id}")
            return self.id

