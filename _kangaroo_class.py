_kangaroo_class.py
#📄 Description:
#Implements a class representing a Kangaroo with a pouch that can hold any object, including another Kangaroo.
print("name : Monalisa.N\n usn : 1AY24AI073 \n section : O ")
class Kangaroo:
    def _init_(self):
        self.pouch_contents = []

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)

    def _str_(self):
        return f"Kangaroo pouch contains: {[str(item) for item in self.pouch_contents]}"

# Testing
kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch(roo)

print(kanga)
print(roo)
