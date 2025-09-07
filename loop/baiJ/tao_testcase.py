import zipfile
import os
from pathlib import Path

def generate_fibonacci(n):
    """Generate first n Fibonacci numbers"""
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

def create_testcase():
    # Create testcase directory
    testcase_dir = Path("testcase")
    testcase_dir.mkdir(exist_ok=True)
    
    # Test cases for different values of n
    test_values = [1, 2, 3, 5, 7, 10, 15, 20]
    
    for i, n in enumerate(test_values, 1):
        # Create input file
        with open(testcase_dir / f"input{i}.txt", "w") as f:
            f.write(str(n))
        
        # Generate Fibonacci sequence
        fib_sequence = generate_fibonacci(n)
        
        # Create expected output file
        with open(testcase_dir / f"output{i}.txt", "w") as f:
            f.write("\n".join(map(str, fib_sequence)))
    
    # Create zip file
    with zipfile.ZipFile("testcase.zip", "w") as zf:
        for file in testcase_dir.glob("*.txt"):
            zf.write(file, file.name)
    
    print(f"Created {len(test_values)} test cases for Fibonacci sequence")

if __name__ == "__main__":
    create_testcase()
