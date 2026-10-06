#!/usr/bin/env python3


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(
        lambda mage: mage["power"] >= min_power,
        mages
    ))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(
        lambda spell: f"* {spell} *",
        spells
    ))


def mage_stats(mages: list[dict]) -> dict:
    powers = list(map(lambda mage: mage["power"], mages))
    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2),
    }


def main() -> None:
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Ancient Wand", "power": 78, "type": "relic"}
    ]

    mages = [
        {"name": "Aeris", "power": 72, "element": "air"},
        {"name": "Ignis", "power": 95, "element": "fire"},
        {"name": "Terra", "power": 61, "element": "earth"},
        {"name": "Aqua", "power": 84, "element": "water"}
    ]

    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} "
        f"({sorted_artifacts[0]['power']} power) comes before "
        f"{sorted_artifacts[1]['name']} "
        f"({sorted_artifacts[1]['power']} power)"
    )

    print("\nTesting power filter...")
    strong_mages = power_filter(mages, 80)
    print(f"Mages with power >= 80: {[m['name'] for m in strong_mages]}")

    print("\nTesting spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(
        f"Max power: {stats['max_power']}, "
        f"Min power: {stats['min_power']}, "
        f"Avg power: {stats['avg_power']}"
    )


if __name__ == "__main__":
    main()
