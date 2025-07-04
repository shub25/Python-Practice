class ABC:
    cnt = 0  # Static variable
    cnt += 1  # Incrementing static variable
    @classmethod
    def increment_count(cls):
        print(ABC.cnt)
        ABC.cnt += 1

    def get_num(self,*args):
        cnt=ABC.cnt
        if len(args) > 0:
            for i in args:
                cnt=cnt+i

        return cnt

ob=ABC()
ob.increment_count()
print(ob.cnt)  # Accessing static variable using object
# print(ob.get_num())  # Accessing static variable using method
print(ob.get_num(5,6,5))  # Accessing static variable with an argument
