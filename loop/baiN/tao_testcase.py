import zipfile
import os
from pathlib import Path

def create_hollow_square(n):
    """Generate hollow square pattern"""
    result = []
    for i in range(n):
        line = ""
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                line += "*"
            else:
                line += " "
        result.append(line)
    return result

def create_testcase():
    # Create testcase directory
    testcase_dir = Path("testcase")
    testcase_dir.mkdir(exist_ok=True)
    
    # Test cases for different square sizes
    test_values = [2, 3, 4, 5, 6, 8, 10]
    
    for i, n in enumerate(test_values, 1):
        # Create input file
        with open(testcase_dir / f"input{i}.txt", "w") as f:
            f.write(str(n))
        
        # Generate hollow square pattern
        square = create_hollow_square(n)
        
        # Create expected output file
        with open(testcase_dir / f"output{i}.txt", "w") as f:
            f.write("\n".join(square))
    
    # Create zip file
    with zipfile.ZipFile("testcase.zip", "w") as zf:
        for file in testcase_dir.glob("*.txt"):
            zf.write(file, file.name)
    
    print(f"Created {len(test_values)} test cases for hollow square pattern")

if __name__ == "__main__":
    create_testcase()
