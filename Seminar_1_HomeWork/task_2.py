# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

# def logical_statement(x, y, z):
#     print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
#     return (not (x or y or z)) == (not x and not y and not z)
# if (logical_statement(0, 0, 0) and logical_statement(0, 0, 1) and logical_statement(0, 1, 0) and 
# logical_statement(0, 1, 1) and logical_statement(1, 0, 0) and logical_statement(1, 0, 1) and
# logical_statement(1, 1, 0) and logical_statement(1, 1, 1)):
#     print("Истинно")
# else:
#     print("Ложно")



result = True
for x in 1, 0:
    for y in 1, 0:
        for z in 1, 0:
            print(f"{x = } {y = } {z = }  {not(x or y or z) == (not x and not y and not z)}")