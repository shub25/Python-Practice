#custom context manager

# class Open_file:
#     def __init__(self, filename, mode='r'):
#         self.filename = filename
#         self.mode = mode


#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file

#     def __exit__(self, exc_type, exc_value, traceback):
#         if self.file:
#             self.file.close() 
# obj=Open_file('test.txt', 'w')
# with obj as f:
#     print('This is the type of f',type(f))
#     f.write('Hello, World!\n')
#     f.write('This is a custom context manager example.\n')
#     print(f.closed)

# print(f.closed)


from contextlib import contextmanager

# Step 1: define generator (NOT decorated)
def open_file_gen(filename, mode='r'):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

# Step 2: convert the generator function into a context manager
print(type(open_file_gen))  # This will show it's a generator function
open_file = contextmanager(open_file_gen)  # ✅ no () here
print(type(open_file))  # This will show it's a context manager
# Step 3: use it
with open_file('test.txt', 'w') as f:
    print('This is the type of f:', type(f))
    f.write('Hello, World!\n')
    f.write('This is a custom context manager example 2.\n')

