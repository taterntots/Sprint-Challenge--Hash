def finder(files, queries):

    # cache = {}
    # result = []

    # # Loop through queries
    # for q_str in queries:
    #     # Loop through the files
    #     for path in files:
    #         if q_str in path:
    #             # Add key with value as 1
    #             cache[q_str] = path
    #         # print(path)

    # print(cache)

    # for q in queries:
    #     if q in cache:
    #         result.append(cache[q])

    # return result

    
    
    # Hash the queries as the key and the file path as the value for quick look up
    
    cache = {}
    results = []
    
    # Add queries to my cache with some value
    # Loop the file paths, if the match a query add that path to the value
    for f in files:
        # Slice the path and set the last item as the key in the cache and the path as the value
        key = f.split('/')
        cache.setdefault(key[-1], []).append(f)    
    # If my querie is in the cache, add the value to a list 
    for q in queries:
        if 'nofile' in q:
            continue
        if q in cache:
            if len(cache[q]) > 1:
                for i in cache[q]:
                    results.append(i)
            else:
                results.append(cache[q][0])
        else:
            continue
    return results


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
