import zipfile
import os
from pathlib import Path

def reverse_number(n):
    """Reverse the digits of a number"""
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return reversed_num

def create_testcase():
    # Create testcase directory
    testcase_dir = Path("testcase")
    testcase_dir.mkdir(exist_ok=True)
    
    # Test cases: various numbers including edge cases
    test_values = [7, 12, 123, 1000, 12345, 54321, 100, 1010, 987654, 1]
    
    for i, n in enumerate(test_values, 1):
        # Create input file
        with open(testcase_dir / f"input{i}.txt", "w") as f:
            f.write(str(n))
        
        # Calculate reversed number
        result = reverse_number(n)
        
        # Create expected output file
        with open(testcase_dir / f"output{i}.txt", "w") as f:
            f.write(str(result))
    
    # Create zip file
    with zipfile.ZipFile("testcase.zip", "w") as zf:
        for file in testcase_dir.glob("*.txt"):
            zf.write(file, file.name)
    
    print(f"Created {len(test_values)} test cases for number reversal")

if __name__ == "__main__":
    create_testcase()
