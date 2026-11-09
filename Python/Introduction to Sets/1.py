def average(array):
    # your code goes here
    array = set(array)
    average = sum(array) / len(array)
    return f"{average:.3f}"
    

