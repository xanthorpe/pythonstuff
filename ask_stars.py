def draw_stars(n,order):
    if order=="increasing":
        for i in range(1,n+1):
            print("*" * i)
    if order=="decreasing":
        for i in range(n,0,-1):
            print("*" * i)
n=int(input("How many rows? "))
order=str(input("Order? "))
draw_stars(n,order)
