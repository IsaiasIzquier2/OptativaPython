
var = int(input("Introduce un número del 1 al 20:"))
list1 = [1, 3, 4, 6, 7]


def checkrange(x, a, b):
    
    if (x >= a) and ( x <= b):

        return True
    

def checklist(x, y):

    for i in y:

        count = 0

        if (i == x) :

            count += 1
        
        if count >=1:

            return True
        


print(checkrange(var, 1, 20))
print(checklist(var, list1))