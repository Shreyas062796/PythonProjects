def function(n):
    if(n <= 1):
        return(1)
    return(function(n-1) + function(n-2))

if __name__ == "__main__":
    x = function(6)
    print(x)
