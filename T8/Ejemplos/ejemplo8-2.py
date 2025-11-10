# Ejemplo función suma números

def sum_num(*args):

    total = 0

    for i in args:

        total += i

    return total

totalSuma = sum_num(234, 234, 324, 32546 ,546 ,5467, 6, 36576, 5435)


print(f"El sumatorio total es:{totalSuma}")