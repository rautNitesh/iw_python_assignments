def iterate(d):
    try:
        if isinstance(d,dict):
            for key,value in d.items():
                print(f"key:{key} and value={value}")
        else:
            raise ValueError("Please provide dictionary")
    except ValueError as error:
        print(error)
    

d={11:'a',22:6,5:9}
iterate(d)