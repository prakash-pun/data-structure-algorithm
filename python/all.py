# all(iterable)
# all(
#     condition(item)
#     for item in iterable
# )

def valid_rgb(rgb):
    '''Receives (r, g, b) tuple, Checks if each rgb int is within (0, 255)'''
    return all(0<= val <=255 for val in rgb)

assert valid_rgb((25, 5, 255)) == True
assert valid_rgb((255, 255, 255)) == True
assert valid_rgb((290, 100, 200)) == False
assert valid_rgb((250, 300, 200)) == False
assert valid_rgb((250, 100, 400)) == False
print("Passed all test")
# print(all(["asdf", ""]))