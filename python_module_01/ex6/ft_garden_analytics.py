#!/usr/bin/python3


class Plant:
    class PlantStats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0
            self._shade_count = 0

        def record_grow(self) -> None:
            self._grow_count += 1

        def record_age(self) -> None:
            self._age_count += 1

        def record_show(self) -> None:
            self._show_count += 1

        def record_shade(self) -> None:
            self._shade_count += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, "
                f"{self._show_count} show"
            )

        def display_shade(self) -> None:
            print(f"{self._shade_count} shade")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._stats = self.PlantStats()
        self._name = name

        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height

        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            return
        self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            return
        self._age = age

    def grow(self) -> None:
        self._height = round(self._height + 2.1, 1)
        self._stats.record_grow()

    def age(self) -> None:
        self._age += 1
        self._stats.record_age()

    def show(self) -> None:
        self._stats.record_show()
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def display_extra_stats(self) -> None:
        pass


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:
        super().__init__(name, height, age)
        self._color = color

    def grow(self) -> None:
        self._height = round(self._height + 8.0, 1)
        self._stats.record_grow()

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")

    def bloom(self) -> None:
        print(f"{self._name} is blooming beautifully!")


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age: int, color: str, seed_count: int
    ) -> None:
        super().__init__(name, height, age, color)
        self._seed_count = seed_count

    def grow(self) -> None:
        self._height = round(self._height + 30.0, 1)
        self._stats.record_grow()

    def age(self) -> None:
        self._age += 20
        self._stats.record_age()

    def show(self) -> None:
        super().show()
        if self._seed_count > 0:
            print(f"Seeds: {self._seed_count}")

    def bloom(self) -> None:
        super().bloom()
        self._seed_count = 42
        print(f"Seeds: {self._seed_count}")


class Tree(Plant):
    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        self._stats.record_shade()
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height}cm long and {self._trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")

    def display_extra_stats(self) -> None:
        self._stats.display_shade()


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self) -> None:
        super().grow()

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant._name}]")
    plant._stats.display()
    plant.display_extra_stats()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(
        f"Is 30 days more than a year? -> "
        f"{Plant.is_older_than_year(30)}"
    )
    print(
        f"Is 400 days more than a year? -> "
        f"{Plant.is_older_than_year(400)}"
    )

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("Rose has not bloomed yet")
    display_statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.show()
    rose.bloom()
    display_statistics(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 0)
    sunflower.show()
    print("Sunflower has not bloomed yet")
    print("Seeds: 0")
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.show()
    sunflower.bloom()
    display_statistics(sunflower)

    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_statistics(anonymous)


if __name__ == "__main__":
    main()
