#!/usr/bin/python3
# Save this code in a file, for example, print_args.py

if __name__ == "__main__":
    import sys

    # Get the number of arguments
    num_args = len(sys.argv) - 1

    # Print the number of arguments
    print(f"Number of argument(s): {num_args}", end='')

    # Print arguments or '.' if no arguments
    if num_args > 0:
        print(" followed by:")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")
    else:
        print(".")

