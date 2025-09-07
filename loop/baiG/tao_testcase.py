import zipfile
import os
from pathlib import Path

def count_digits(n):
    """Count digits in a positive integer"""
    count = 0
    temp = n
    while temp > 0:
        count += 1
        temp //= 10
    return count

def create_testcase():
    # Create testcase directory
    testcase_dir = Path("testcase")
    testcase_dir.mkdir(exist_ok=True)
    
    # Test cases: various numbers to count digits
    test_numbers = [
        1,      # 1 digit
        9,      # 1 digit
        10,     # 2 digits
        99,     # 2 digits
        100,    # 3 digits
        999,    # 3 digits
        1000,   # 4 digits
        12345,  # 5 digits
        987654, # 6 digits
        1000000 # 7 digits
    ]
    
    for i, n in enumerate(test_numbers, 1):
        # Create input file
        with open(testcase_dir / f"input{i}.txt", "w") as f:
            f.write(str(n))
        
        # Create expected output file
        result = count_digits(n)
        with open(testcase_dir / f"output{i}.txt", "w") as f:
            f.write(str(result))
    
    # Create zip file
    with zipfile.ZipFile("testcase.zip", "w") as zf:
        for file in testcase_dir.glob("*.txt"):
            zf.write(file, file.name)
    
    print(f"Created {len(test_numbers)} test cases for digit counting")

if __name__ == "__main__":
    create_testcase()
