# Enter your code here. Read input from STDIN. Print output to STDOUT


if __name__ == "__main__":
    n,d = map(int,raw_input().split())
    ar = map(int,raw_input().split())
    output = 0
    for i in ar[0:-2]:
        if i+d in ar and i+2*d in ar:
            output += 1
    print output
