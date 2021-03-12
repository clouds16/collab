def reverseList( mylist): 

    def reverse(mylist, start, end):
        if start < end:
            temp = mylist[start]
            mylist[start] = mylist[end]
            mylist[end] = temp
            start += 1
            end -=1
            reverse(mylist, start, end)
            
        return mylist

    return reverse(mylist, 0 , len(mylist)-1)


def reverseAList(mylist):

    if 0 < len(mylist)-1:
        temp = mylist[0]
        mylist[0] = mylist[-1]
        mylist[-1] = temp
        return reverseAList(mylist[1:-1])
    
    return mylist
        

def main():
    l = [1,2,3,4,5,6,7,8,9]
    print(reverseList(l))
    #print(reverseAList(l))

main()