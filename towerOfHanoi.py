#Solving the tower of hanoi problem for a given n

def hanoi(n, src, dest, aux):
    if(n == 1):
        print "Move from ", src," to ", dest
        return
    else:
        hanoi(n-1, src, aux, dest)
        print "Move from ",src , " to ", dest
        hanoi(n-1, aux, dest, src)

if __name__ == "__main__":
    n = input("Enter number of disks:")
    hanoi(n, "left", "center", "right")
