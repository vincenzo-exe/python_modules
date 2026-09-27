#!/usr/bin/python3


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:

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

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")

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


def main() -> None:
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15.0, 10)
    plant.show()
    plant.set_height(25.0)
    print(f"Height updated: {plant.get_height():g}cm")
    plant.set_age(30)
    print(f"Age updated: {plant.get_age()} days")
    plant.set_height(-5)
    print("Height update rejected")
    plant.set_age(-10)
    print("Age update rejected")
    plant.show()


if __name__ == "__main__":
    main()
