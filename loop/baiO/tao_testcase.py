import zipfile
import os
from pathlib import Path

def gcd(a, b):
    """Calculate GCD using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Calculate LCM using GCD"""
    return (a * b) // gcd(a, b)

def create_testcase():
    # Create testcase directory
    testcase_dir = Path("testcase")
    testcase_dir.mkdir(exist_ok=True)
    
    # Test cases: various pairs of numbers
    test_pairs = [
        (12, 18),
        (15, 25),
        (6, 9),
        (10, 15),
        (7, 13),
        (20, 30),
        (8, 12),
        (14, 21),
        (100, 150),
        (17, 19)
    ]
    
    for i, (a, b) in enumerate(test_pairs, 1):
        # Create input file
        with open(testcase_dir / f"input{i}.txt", "w") as f:
            f.write(f"{a} {b}")
        
        # Calculate LCM
        result = lcm(a, b)
        
        # Create expected output file
        with open(testcase_dir / f"output{i}.txt", "w") as f:
            f.write(str(result))
    
    # Create zip file
    with zipfile.ZipFile("testcase.zip", "w") as zf:
        for file in testcase_dir.glob("*.txt"):
            zf.write(file, file.name)
    
    print(f"Created {len(test_pairs)} test cases for LCM calculation")

if __name__ == "__main__":
    create_testcase()
