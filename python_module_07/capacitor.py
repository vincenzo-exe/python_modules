#!/usr/bin/python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing(factory: HealingCreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(f"Testing Creature with healing capability base: {base.describe()}")
    print(base.attack())
    print(base.heal())

    print(f"evolved: {evolved.describe()}")
    print(evolved.attack())
    print(evolved.heal())


def test_transform(factory: TransformCreatureFactory) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(f"Testing Creature with transform capability base: "
          f"{base.describe()}")
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print(f"evolved: {evolved.describe()}")
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def main() -> None:
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    test_healing(healing_factory)
    test_transform(transform_factory)


if __name__ == "__main__":
    main()
