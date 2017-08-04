import sys
def test(did_pass):
    """Print the result of a test."""
    lineum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok".format(lineum)
    else:
        msg = ("Test at line {0} FAILED.".format(lineum))
    print(msg)
def add_fruit(inventory, fruit, quantity=0):
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity
    return


# Make these tests work...
new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)
test('strawberries' in new_inventory) == True
test( new_inventory['strawberries'] == 10)
add_fruit(new_inventory, 'strawberries', 25)
test( new_inventory['strawberries'] == 35)

