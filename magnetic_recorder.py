def solve(disk):
   order = list(range(len(disk)))   
   order.sort(key=lambda x: disk[x], reverse=False)
   print(order)

def main():
    disk = [10,1,5,9,2,4,15,7]
    solve(disk)
if __name__ == "__main__":
    main()