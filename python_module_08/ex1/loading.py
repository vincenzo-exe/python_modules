#!/usr/bin/python3

import importlib
from typing import Any


def check_dependency(package_name: str) -> tuple[bool, str]:
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, "__version__", "unknown")
        return True, version
    except ImportError:
        return False, "Not installed"


def check_dependencies() -> bool:
    packages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
    }

    all_installed = True

    print("Checking dependencies:")

    for package, description in packages.items():
        installed, version = check_dependency(package)

        if installed:
            print(f"[OK] {package} ({version}) - {description}")
        else:
            print(f"[MISSING] {package} - Not installed")
            all_installed = False

    return all_installed


def generate_matrix_data(size: int) -> Any:
    numpy = importlib.import_module("numpy")
    pandas = importlib.import_module("pandas")

    dataframe = pandas.DataFrame({
        "time": numpy.arange(size),
        "signal_strength": numpy.random.normal(100, 15, size),
        "system_load": numpy.random.uniform(20, 95, size),
        "anomaly_score": numpy.random.randint(0, 2, size),
    })

    return dataframe


def analyze_matrix_data(dataframe: Any) -> None:
    signal_mean = dataframe["signal_strength"].mean()
    load_mean = dataframe["system_load"].mean()
    anomaly_count = dataframe["anomaly_score"].sum()

    print("Analyzing Matrix data...")
    print(f"Processing {len(dataframe)} data points...")
    print(f"Average signal strength: {signal_mean:.2f}")
    print(f"Average system load: {load_mean:.2f}")
    print(f"Anomalies detected: {anomaly_count}")


def create_visualization(dataframe: Any) -> None:
    matplotlib = importlib.import_module("matplotlib.pyplot")

    print("Generating visualization...")

    matplotlib.plot(
        dataframe["time"],
        dataframe["signal_strength"],
    )
    matplotlib.xlabel("Time")
    matplotlib.ylabel("Signal Strength")
    matplotlib.title("Matrix Signal Analysis")
    matplotlib.savefig("matrix_analysis.png")
    matplotlib.close()


def show_dependency_management() -> None:
    print("Dependency management comparison:")
    print("- pip uses requirements.txt")
    print("- Poetry uses pyproject.toml")


def main() -> None:
    print("LOADING STATUS: Loading programs...")

    if not check_dependencies():
        print()
        print("Missing dependencies.")
        print("Install with pip:")
        print("pip install -r requirements.txt")
        print()
        print("Install with Poetry:")
        print("poetry install")
        print("poetry run python loading.py")
        return

    show_dependency_management()

    dataframe = generate_matrix_data(1000)
    analyze_matrix_data(dataframe)
    create_visualization(dataframe)

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
