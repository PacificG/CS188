# Comment: This is a fairly simple Python script

print('Hello, World!')

def quicksort(ls):
    if len(ls) <= 1:
        return ls
    else:
        return quicksort([x for x in ls if x<ls[0]]) + [ls[0]] + quicksort([x for x in ls if x > ls[0]]) 
        