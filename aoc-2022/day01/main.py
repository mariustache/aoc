
if __name__ == "__main__":
    calories_data = list()
    with open("./input.txt", "r") as handle:
        calories_data = [inventory.split("\n") for inventory in handle.read().split("\n\n")]
    
    print(f"[part1] Total calories: {max([sum([int(item) for item in inventory]) for inventory in calories_data])}")
    print(f"[part2] Total calories: {sum(sorted([sum([int(item) for item in inventory]) for inventory in calories_data], reverse=True)[0:3])}")
