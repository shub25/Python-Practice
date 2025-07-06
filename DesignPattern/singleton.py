# import threading
# from functools import wraps

# # Method 1: Using threading.Lock (Simple but with performance overhead)
# class ThreadSafeSingleton1:
#     _instance = None
#     _lock = threading.Lock()
    
#     def __new__(cls):
#         if cls._instance is None:
#             with cls._lock:
#                 # Double-checked locking pattern
#                 if cls._instance is None:
#                     cls._instance = super().__new__(cls)
#         return cls._instance
    
#     def __init__(self):
#         # Initialize only once
#         if not hasattr(self, 'initialized'):
#             self.initialized = True
#             # Your initialization code here
#             print("Singleton initialized")

# # Method 2: Using threading.RLock (Reentrant lock)
# class ThreadSafeSingleton2:
#     _instance = None
#     _lock = threading.RLock()
    
#     def __new__(cls):
#         if cls._instance is None:
#             with cls._lock:
#                 if cls._instance is None:
#                     cls._instance = super().__new__(cls)
#         return cls._instance

# # Method 3: Using __call__ method (Decorator pattern)
# class SingletonMeta(type):
#     _instances = {}
#     _lock = threading.Lock()
    
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             with cls._lock:
#                 if cls not in cls._instances:
#                     cls._instances[cls] = super().__call__(*args, **kwargs)
#         return cls._instances[cls]

# class ThreadSafeSingleton3(metaclass=SingletonMeta):
#     def __init__(self):
#         print("Singleton initialized")

# # Method 4: Using threading.local for thread-local singletons
# class ThreadLocalSingleton:
#     _local = threading.local()
    
#     def __new__(cls):
#         if not hasattr(cls._local, 'instance'):
#             cls._local.instance = super().__new__(cls)
#         return cls._local.instance

# # Method 5: Module-level singleton (Pythonic way)
# # This is naturally thread-safe because modules are imported once
# class _ModuleSingleton:
#     def __init__(self):
#         self.initialized = True
#         print("Module singleton initialized")
    
#     def do_something(self):
#         return "Module singleton working"

# # Export the instance
# module_singleton = _ModuleSingleton()

# # Method 6: Using @property and threading.Lock
# class ThreadSafeSingleton6:
#     _instance = None
#     _lock = threading.Lock()
    
#     @classmethod
#     def get_instance(cls):
#         if cls._instance is None:
#             with cls._lock:
#                 if cls._instance is None:
#                     cls._instance = cls()
#         return cls._instance
    
#     def __init__(self):
#         if hasattr(self, 'initialized'):
#             raise Exception("Singleton already initialized")
#         self.initialized = True

# # Method 7: Using once_flag pattern (inspired by C++)
# class OnceFlag:
#     def __init__(self):
#         self._lock = threading.Lock()
#         self._called = False
    
#     def call_once(self, func, *args, **kwargs):
#         if not self._called:
#             with self._lock:
#                 if not self._called:
#                     func(*args, **kwargs)
#                     self._called = True

# class ThreadSafeSingleton7:
#     _instance = None
#     _once_flag = OnceFlag()
    
#     def __new__(cls):
#         def create_instance():
#             cls._instance = super(ThreadSafeSingleton7, cls).__new__(cls)
        
#         cls._once_flag.call_once(create_instance)
#         return cls._instance

# # Method 8: Using threading.Event for coordination
# class ThreadSafeSingleton8:
#     _instance = None
#     _creation_event = threading.Event()
#     _lock = threading.Lock()
    
#     def __new__(cls):
#         if cls._instance is None:
#             with cls._lock:
#                 if cls._instance is None:
#                     cls._instance = super().__new__(cls)
#                     cls._creation_event.set()
#         else:
#             # Wait for creation to complete if another thread is creating
#             cls._creation_event.wait()
#         return cls._instance

# # Testing function
# def test_singleton(singleton_class, thread_count=10):
#     instances = []
    
#     def create_instance():
#         if hasattr(singleton_class, 'get_instance'):
#             instance = singleton_class.get_instance()
#         else:
#             instance = singleton_class()
#         instances.append(instance)
    
#     threads = []
#     for i in range(thread_count):
#         thread = threading.Thread(target=create_instance)
#         threads.append(thread)
#         thread.start()
    
#     for thread in threads:
#         thread.join()
    
#     # Check if all instances are the same
#     all_same = all(instance is instances[0] for instance in instances)
#     print(f"All instances are the same: {all_same}")
#     print(f"Number of unique instances: {len(set(id(instance) for instance in instances))}")

# # Example usage
# if __name__ == "__main__":
#     print("Testing ThreadSafeSingleton1:")
#     test_singleton(ThreadSafeSingleton1)
    
#     print("\nTesting ThreadSafeSingleton3 (Metaclass):")
#     test_singleton(ThreadSafeSingleton3)
    
#     print("\nTesting ThreadSafeSingleton6 (Class method):")
#     test_singleton(ThreadSafeSingleton6)
    
#     print("\nUsing module singleton:")
#     print(module_singleton.do_something())

import threading 
class Singleton:
    _instance=None
    _lock=threading.Lock()

    '''
    we will use the __new__ method to create a singleton class. __new__ method
    is responsible for creating a new instance of the class. It is called before
    __init__ method. So __new__ method is the actual method that creates the instance.
    Whereas __init__ method is used to initialize the instance.

    Note: object is the base class for all classes in Python.We know that everything
    in Python is an object. So classes are also objects. If we ever want to control how 
    the objects are actually created we can override the __new__ method.
    '''

    def __new__(cls,*args,**kwargs):
        #  first we check if the instance is already created or not. This is a thread safe 
        # check. If the instance is not created then we will create it.
        print("Creating instance of Singleton class")
        if not cls._instance:
            # if instance is not created then we will acquire the lock to create it.
            with cls._lock:
                # okay even though we have acquired the lock we need to recheck if
                # the instance is created or not. The reason is to in multi-threaded environment
                # multiple threads can reach here and they can create multiple instances.
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                
        return cls._instance
    
    def __init__(self,value):
        if not hasattr(self,'initialized'):
            print("Initializing Singleton class")
            self.value = value
            self.initialized = True


def test_singleton(value):
    obj= Singleton(value)
    print(obj.value)

thread1=threading.Thread(target=test_singleton,args=("Thread1",))
thread2=threading.Thread(target=test_singleton, args=("Thread2",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
