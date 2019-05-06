def main():
    """ Main function """

    nums = []

    # Get an integer
    i = int(input("Enter a number: "), 10)

    # Populate the list
    print(f"Enter {i} numbers: ")
    for c in range(i):
        nums.append(int(input(), 10))
    
    # Sort the list
    rearrange(nums, i)

    #Print out the list one at a time.
    for c in range(i):
        print(f"{nums[c]}")


def rearrange(int_list, n):
    """ rearrange the list using the number of ones in the binary equivalent of the integers """
    
    c = 0
    d = 0
    
    # Loop through the list swapping its element where needed.
    for c in range(n-1):
        for d in range(n-c-1):
            if num_of_ones(int_list[d]) > num_of_ones(int_list[d+1]):
                # Swap
                int_list[d], int_list[d+1] = int_list[d+1], int_list[d]
            elif num_of_ones(int_list[d]) == num_of_ones(int_list[d+1]) and int_list[d] > int_list[d+1]:
                # Swap
                int_list[d], int_list[d+1] = int_list[d+1], int_list[d]

    return int_list



def num_of_ones(n):
    """ Calculate the number of ones in the binary equivalent of an integer """
    
    # Convert n into a binary string.
    m = format(n, 'b')
    # Get the numbers of ones in the binary string.
    counter = m.count('1')

    return counter


if __name__ == "__main__":
    main()