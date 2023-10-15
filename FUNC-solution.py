def flatten_and_sort(lst):
    out = []
    for item in lst:
        if type(item) == list:
            for i in item:
                out.append(i)
        else:
            out.append(item)

    return sorted(out)

nested = [0,-2,5,4, [5,344,4,19], [215, 8585965]]

out = flatten_and_sort(nested)
print(out)
print(nested)

'''
How does this solution ensure data immutability?
    This solution ensures data immutability because it does not modify the original list lst. 
    It creates a new list flattened, which contains the flattened and sorted elements, and returns this new list, 
    leaving the original list unchanged.

Is this solution a pure function? Why or why not?
    This solution is not a pure function because it sorts the flattened list in place,
    which can have side effects if the original list is used elsewhere.

Is this solution a higher order function? Why or why not?
    This solution is not a higher-order function because it neither takes functions 
    as arguments nor returns a function as its result.

Would it have been easier to solve this problem using a different programming style?
    It could be argued that solving this problem using a different programming style,
    but it depends on the specific requirements and constraints of the problem.

Why in particular is functional programming a helpful paradigm when solving this problem?
    Functional programming is helpful for this problem because it encourages immutability, preventing side effects, 
    and it promotes code modularity and readability by breaking down tasks into smaller functions. Additionally, 
    functional code tends to be more concise and reusable, facilitating adaptability for similar tasks.

'''