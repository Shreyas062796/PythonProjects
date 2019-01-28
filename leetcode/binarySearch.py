def search(nums, target):
    start = 0
    end = len(nums)-1
    while(start <= end):
        mid = (start + end)//2
        if(target == nums[mid]):
            return(mid)
        if(nums[mid] > target):
            end = mid-1
        else:
            start = mid+1
        print(start)
        print(mid)
    return(-1)


if __name__ == "__main__":
    print(search([-1,0,3,5,9,12],2))