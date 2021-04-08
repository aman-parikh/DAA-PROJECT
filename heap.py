#methods to select optimal path
def swap(spot_list,x,y):
    t=spot_list[x]
    spot_list[x]=spot_list[y]
    spot_list[y]=t

def min_heapify(spot_list,ind,limit):
    l=2*ind+1
    r=2*ind+2
    minIndex=ind
    if(l<limit and spot_list[l].value<spot_list[minIndex].value):
        minIndex=l
    if(r<limit and spot_list[r].value<spot_list[minIndex].value):
        minIndex=r
    if(minIndex!=ind):
        swap(spot_list,ind,minIndex)
        min_heapify(spot_list,minIndex,limit)
    else:
        return

def build_min_heap(spot_list,n):
    for i in range(n//2,-1,-1):
        min_heapify(spot_list,i,n)

def extract_min_util(spot_list,size):
    if size==0:
        return
    swap(spot_list,0,size-1)
    min_heapify(spot_list,0,size-1)

def extract_min(spot_list,size):
    extract_min_util(spot_list,size)
    return spot_list[0]
