import zipfile
import os
from pathlib import Path

def is_prime(n):
    """Check if n is prime"""
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

def create_testcase():
    # Create testcase directory
    testcase_dir = Path("testcase")
    testcase_dir.mkdir(exist_ok=True)
    
    # Test cases: mix of prime and non-prime numbers
    test_values = [1, 2, 3, 4, 7, 9, 11, 12, 17, 25, 29, 100, 101, 997]
    
    for i, n in enumerate(test_values, 1):
        # Create input file
        with open(testcase_dir / f"input{i}.txt", "w") as f:
            f.write(str(n))
        
        # Check if prime
        result = "YES" if is_prime(n) else "NO"
        
        # Create expected output file
        with open(testcase_dir / f"output{i}.txt", "w") as f:
            f.write(result)
    
    # Create zip file
    with zipfile.ZipFile("testcase.zip", "w") as zf:
        for file in testcase_dir.glob("*.txt"):
            zf.write(file, file.name)
    
    print(f"Created {len(test_values)} test cases for prime checking")

if __name__ == "__main__":
    create_testcase()
