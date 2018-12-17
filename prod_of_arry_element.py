#Product of array elements
#Return the product of array elements under a given modulo.
#That is, return (Array[0]*Array[1]*Array[2]...*Array[n])%modulo
def product(arr,n,mod):
    # your code here
    pro=1
    for j in range(0,n):
        pro=pro*arr[j]
        if pro>=mod:
            pro=pro%mod
    return pro
	
{
#Initial Template for Python 3
if __name__=="__main__":
    t=int(input())
    mod=1000000007
    for j in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        print(product(arr,n,mod))
}
