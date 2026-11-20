def print_formatted(number):
    # your code goes here
    width = len(f"{number:b}")
    for i in range(1, number + 1):
        print(
            f"{i:>{width}} "
            f"{i:>{width}o} "
            f"{i:>{width}X} "
            f"{i:>{width}b}"    
            )
      

