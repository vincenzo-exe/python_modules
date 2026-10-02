#!/usr/bin/python3

from abc import ABC, abstractmethod
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._rank = 0

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No data available")

        value = self._data.pop(0)
        result = (self._rank, value)
        self._rank += 1
        return result

    def stats(self) -> tuple[int, int]:
        total = self._rank + len(self._data)
        remaining = len(self._data)
        return total, remaining


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            return all(
                isinstance(item, (int, float))
                for item in data
            )

        return False

    def ingest(
        self, data: int | float | list[int | float]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._data.append(str(item))
        else:
            self._data.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)

        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self._data.append(item)
        else:
            self._data.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return self._validate_log(data)

        if isinstance(data, list):
            return all(
                isinstance(item, dict) and self._validate_log(item)
                for item in data
            )

        return False

    def _validate_log(self, data: dict[str, str]) -> bool:
        if "log_level" not in data or "log_message" not in data:
            return False

        return all(
            isinstance(key, str) and isinstance(value, str)
            for key, value in data.items()
        )

    def ingest(
        self, data: dict[str, str] | list[dict[str, str]]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, list):
            for item in data:
                self._data.append(
                    f"{item['log_level'].strip()}: "
                    f"{item['log_message']}"
                )
        else:
            self._data.append(
                f"{data['log_level'].strip()}: "
                f"{data['log_message']}"
            )


class ExportPlugin(typing.Protocol):
    def process_output(
        self, data: list[tuple[int, str]]
    ) -> None:
        ...


class CSVPlugin:
    def process_output(
        self, data: list[tuple[int, str]]
    ) -> None:
        values = []

        for _, value in data:
            values.append(value)

        print(f"CSV Output: {','.join(values)}")


class JSONPlugin:
    def process_output(
        self, data: list[tuple[int, str]]
    ) -> None:
        values = []

        for rank, value in data:
            values.append(f'"item_{rank}": "{value}"')

        result = ", ".join(values)
        print(f"JSON Output: {{{result}}}")


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(
        self, stream: list[typing.Any]
    ) -> None:
        for element in stream:
            processed = False

            for processor in self._processors:
                if processor.validate(element):
                    processor.ingest(element)
                    processed = True
                    break

            if not processed:
                print(
                    "DataStream error - Can't process element "
                    f"in stream: {element}"
                )

    def output_pipeline(
        self,
        nb: int,
        plugin: ExportPlugin
    ) -> None:
        for processor in self._processors:
            data = []

            for _ in range(nb):
                try:
                    data.append(processor.output())
                except IndexError:
                    break

            if data:
                plugin.process_output(data)

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self._processors:
            print("No processor found, no data")
            return

        for processor in self._processors:
            total, remaining = processor.stats()
            name = processor.__class__.__name__
            print(
                f"{name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")

    data_stream = DataStream()
    data_stream.print_processors_stats()

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("Registering Processors")
    data_stream.register_processor(numeric)
    data_stream.register_processor(text)
    data_stream.register_processor(log)

    stream = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected"
            }
        ],
        42,
        ["Hi", "five"]
    ]

    print("Send first batch of data on stream:")
    print(stream)
    data_stream.process_stream(stream)

    data_stream.print_processors_stats()

    print(
        "Send 3 processed data from each processor "
        "to a CSV plugin:"
    )

    csv = CSVPlugin()
    data_stream.output_pipeline(3, csv)

    data_stream.print_processors_stats()

    stream = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": " ERROR",
                "log_message": "500 server crash"
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days"
            }
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello"
    ]

    print("Send another batch of data:")
    print(stream)
    data_stream.process_stream(stream)

    data_stream.print_processors_stats()

    print(
        "Send 5 processed data from each processor "
        "to a JSON plugin:"
    )

    json_plugin = JSONPlugin()
    data_stream.output_pipeline(5, json_plugin)

    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
