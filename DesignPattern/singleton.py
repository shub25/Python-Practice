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
