def finder(files, queries):

    cache = {}
    result = []

    # Loop through queries
    for q_str in queries:
        # print('q_str', q_str)
        # Loop through the files
        for path in files:
            if q_str in path:
                # Add key with value as 1
                cache[q_str] = path
                # print(cache)
                # result.append(path)
            # print(path)

    print(cache)

    for q in queries:
        if q in cache:
            result.append(cache[q])

    return result


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
