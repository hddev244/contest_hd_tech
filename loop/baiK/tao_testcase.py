import zipfile
import os
from pathlib import Path

def create_triangle(n):
    """Generate triangle pattern"""
    result = []
    for i in range(1, n + 1):
        result.append("*" * i)
    return result

def create_testcase():
    # Create testcase directory
    testcase_dir = Path("testcase")
    testcase_dir.mkdir(exist_ok=True)
    
    # Test cases for different triangle sizes
    test_values = [1, 2, 3, 4, 5, 7, 10]
    
    for i, n in enumerate(test_values, 1):
        # Create input file
        with open(testcase_dir / f"input{i}.txt", "w") as f:
            f.write(str(n))
        
        # Generate triangle pattern
        triangle = create_triangle(n)
        
        # Create expected output file
        with open(testcase_dir / f"output{i}.txt", "w") as f:
            f.write("\n".join(triangle))
    
    # Create zip file
    with zipfile.ZipFile("testcase.zip", "w") as zf:
        for file in testcase_dir.glob("*.txt"):
            zf.write(file, file.name)
    
    print(f"Created {len(test_values)} test cases for triangle pattern")

if __name__ == "__main__":
    create_testcase()
