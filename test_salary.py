import sys
from salary import calculate_bonus

def test_calculate_bonus():
    # Test case 1: rating below threshold
    assert calculate_bonus(2.5, 10, 50000, else_value=0) == 0

    # Test case 2: rating above threshold
    assert calculate_bonus(4.0, 10, 60000, else_value=0) == 6000

def test_main():
    test_calculate_bonus()

if __name__ == "__main__":
    test_main()