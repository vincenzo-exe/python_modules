#!/usr/bin/python3


class Plant:
    def __init__(
        self, name: str, height: float, age_days: int, growth_rate: float
    ) -> None:
        self.name = name
        self.height = height
        self.age_days = age_days
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.age_days += 1


if __name__ == "__main__":
    plant = Plant("Rose", 25.0, 30, 0.8)

    print("=== Garden Plant Growth ===")
    plant.show()

    initial_height = plant.height

    for day in range(7):
        print(f"=== Day {day + 1} ===")
        plant.grow()
        plant.age()
        plant.show()
    growth = round(plant.height - initial_height, 1)
    print(f"Growth this week: {growth}cm")
