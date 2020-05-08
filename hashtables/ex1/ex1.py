def get_indices_of_item_weights(weights, length, limit):
  
    # cache = {}

    # for index, w in enumerate(weights):
    #     cache[w] = index
    #     print(cache)
    #     target = limit - w
    #     print(target)

    #     for key, value in cache.items():
    #         # print(key, value)
    #         if key == target:
    #             return (cache[w], value)

    # return None

    cache = {}
    # Hash weights first for easy lookup 
    # Enumerate to pass index as value
    # For loop the subtraction 
    # Limit - place in the loop, look to see if that exists in the hash table and spit out that index as the answer
    for index, v in enumerate(weights):
        cache.setdefault(v, []).append(index)
    for i in weights:
        target = limit - i
        if target in cache:
            if cache[target] > cache[i]:
                if len(cache[target]) > 1 and len(cache[i]) > 1:
                    return (cache[target][0], cache[i][1])
                return (cache[target][0], cache[i][0])
            else:
                if len(cache[target]) > 1 and len(cache[i]) > 1:
                    return (cache[i][1], cache[target][0])
                return (cache[i][0], cache[target][0])
    return None

weights_2 = [4, 4]
weights_3 = [4, 6, 10, 15, 16, 21]

print(get_indices_of_item_weights(weights_2, 2, 8))
# print(get_indices_of_item_weights(weights_3, 6, 21))

# (3, 1)

# Given a package with a weight limit `limit` and a list `weights` of item
# weights, implement a function `get_indices_of_item_weights` that finds
# two items whose sum of weights equals the weight limit `limit`. Your
# function will return an instance of an `Answer` tuple that has the
# following form:

# ```
# (zero, one)
# ```

# where each element represents the item weights of the two packages.
# _**The higher valued index should be placed in the `zeroth` index and
# the smaller index should be placed in the `first` index.**_ If such a
# pair doesn’t exist for the given inputs, your function should return
# `None`.

# Your solution should run in linear time.

# Example:
# ```
# input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
# output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
# ```