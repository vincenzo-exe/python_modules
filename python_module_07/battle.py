#!/usr/bin/python3

from ex0 import AquaFactory, FlameFactory
from ex0.factories import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing factory")
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())


def test_battle(
    flame_factory: CreatureFactory,
    aqua_factory: CreatureFactory,
) -> None:
    flame = flame_factory.create_base()
    aqua = aqua_factory.create_base()

    print("Testing battle")
    print(flame.describe())
    print("vs.")
    print(aqua.describe())
    print("fight!")
    print(flame.attack())
    print(aqua.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    test_factory(aqua_factory)
    test_battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
