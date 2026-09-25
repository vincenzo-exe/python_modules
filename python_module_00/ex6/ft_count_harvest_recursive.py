def ft_count_harvest_recursive() -> None:
    days: int = int(input("Days until harvest: "))

    def count(day: int) -> None:
        if day == days:
            print("Harvest time!")
            return
        print(f"Day {day + 1}")
        count(day + 1)
    count(0)
