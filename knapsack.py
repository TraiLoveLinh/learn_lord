class Item:
    def __init__(self, weight, profit) -> None:
        self.weight = weight
        self.profit = profit


def knapsack(items, W):
    items.sort(key=lambda x: x.profit/x.weight, reverse=True)
    finallValue = 0
    for item in items:
        if item.weight <= W:
            finallValue += item.profit
            W -= item.weight
        else:
            finallValue += (W/item.weight)*item.profit
            break
    return finallValue


def main():
    items = [Item(10, 20), Item(20, 30), Item(30, 66), Item(40, 40), Item(50, 60)]
    print(knapsack(items, 100))


if __name__ == "__main__":
    main()
