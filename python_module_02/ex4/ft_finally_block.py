#!/usr/bin/python3


class PlantError(Exception):
    pass


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    print("Testing valid plants...")
    print("Opening watering system")

    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")

        print("Testing invalid plants...")
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrots")

    except PlantError as e:
        print(f"Caught PlantError: {e} .. ending tests and returning to main")
        return

    finally:
        print("Closing watering system")

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
