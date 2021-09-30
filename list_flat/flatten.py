nests = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(container):
    for i in container:
        if isinstance(i, (list,tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i

print(list(flatten(nests)))