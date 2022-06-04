def processInput():
    try:
        steps=int(input('Number of steps for pi calculation: '))
    except ValueError as e:
        print('Integer convertion error: {}'.format(e))
        exit(1)

    if steps<=0:
       print('Steps cannot be non-positive')
       exit(2)

    return steps
