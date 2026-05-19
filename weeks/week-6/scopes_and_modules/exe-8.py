# 8. Inspecting a module. Given any imported module m, write a function public_names(m) that returns a
# sorted list of attribute names on m that do not start with an underscore.


def public_names(m):
    try:
        attributes = m.__dict__
    except AttributeError:
        return None
    
    return [attribute for attribute in attributes if not attribute.startswith('__')]

import math 
print(public_names(math))