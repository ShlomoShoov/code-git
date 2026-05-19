# 9. Avoid the mutable-default gotcha. The following function is buggy because of how scopes and default
# arguments interact. Explain the bug and fix it.

def add_item(item, bag=[]):
    bag.append(item)
    return bag

print(add_item('bag'))

# fix:

def add_item_fixed(item, bag=None):
    if  bag is None:
        return [item]
    else:
        bag.append(item)
