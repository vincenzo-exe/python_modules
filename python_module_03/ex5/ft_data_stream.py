#!/usr/bin/python3

import random
import typing

players = ["alice", "bob", "charlie", "dylan"]
actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "use"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        event = events[index]
        del events[index]
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_generator = gen_event()

    for i in range(1000):
        event = next(event_generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    event_generator = gen_event()
    events = []

    for _ in range(10):
        events += [next(event_generator)]

    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
