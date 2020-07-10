#Tower of hanoi

def toh(n, from_rod, to_rod , through_rod):
    if n==1:
        print(f"Move 1 from {from_rod} to {to_rod}")
        return
    toh(n-1,from_rod, through_rod, to_rod)
    print(f"Move {n} from {from_rod} to {to_rod}\n")
    toh( n-1 , through_rod, to_rod, from_rod)
    

toh(3,'A','B','C')
