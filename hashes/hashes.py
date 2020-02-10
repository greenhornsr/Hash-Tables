import hashlib

# b means it is a byte like object.  to hash a string you have to do this. You can also use .encode() or .encode(utf-8)
# i.e.  key = "string of some sort".encode() 
key = b"str"
my_string = "this is a normal string, Nothing to see here.".encode()

for i in range(10):
    hashed = hashlib.sha256(key).hexdigest()
    print(hashed)
    # breakpoint() will activate python de bug so we can use dir(); in this scenario dir(hashed)
    # breakpoint()

for i in range(10):
    hashed = hash(key)
    print(hashed % 8)
