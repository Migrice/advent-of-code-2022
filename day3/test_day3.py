from .day3 import day3_part1


def test_day3_part1_is_16():
    assert (day3_part1("vJrwpWtwJgWrhcsFMMfFFhFp")) == 16


def test_day3_part1_is_38():
    assert (day3_part1("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")) == 38


def test_day3_part1_is_42():
    assert (day3_part1("PmmdzqPrVvPwwTWBwg")) == 42


def test_day3_part1_is_22():
    assert (day3_part1("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn")) == 22


def test_day3_part1_is_20():
    assert (day3_part1("ttgJtRGJQctTZtZT")) == 20


def test_day_3_part1_is_19():
    assert (day3_part1("CrZsJsPPZsGzwwsLwLmpwMDw")) == 19
