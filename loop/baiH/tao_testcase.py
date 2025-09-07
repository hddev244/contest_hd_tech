import zipfile
import os
from pathlib import Path
import random

def find_min(numbers):
    """Find minimum number in a list"""
    min_num = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < min_num:
            min_num = numbers[i]
    return min_num

def create_testcase():
    # Create testcase directory
    testcase_dir = Path("testcase")
    testcase_dir.mkdir(exist_ok=True)
    
    # Test cases
    test_cases = [
        ([3, 7, 1, 9, 2], 1),
        ([-5, -2, -10, -1], -10),
        ([100], 100),
        ([5, 5, 5, 5], 5),
        ([1, 2, 3, 4, 5], 1),
        ([10, 9, 8, 7, 6], 6),
        ([-1, -2, -3, -4, -5], -5),
        ([0, 1, -1, 2, -2], -2),
        ([100, 50, 25, 12, 6, 3, 1], 1),
        ([random.randint(-100, 100) for _ in range(10)], None)
    ]
    
    for i, (numbers, expected) in enumerate(test_cases, 1):
        # Calculate expected result if not provided
        if expected is None:
            expected = find_min(numbers)
        
        # Create input file
        with open(testcase_dir / f"input{i}.txt", "w") as f:
            f.write(f"{len(numbers)}\n")
            f.write(" ".join(map(str, numbers)))
        
        # Create expected output file
        with open(testcase_dir / f"output{i}.txt", "w") as f:
            f.write(str(expected))
    
    # Create zip file
    with zipfile.ZipFile("testcase.zip", "w") as zf:
        for file in testcase_dir.glob("*.txt"):
            zf.write(file, file.name)
    
    print(f"Created {len(test_cases)} test cases for finding minimum")

if __name__ == "__main__":
    create_testcase()
