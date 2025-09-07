import zipfile
import os
from pathlib import Path

def create_testcase():
    # Create testcase directory
    testcase_dir = Path("testcase")
    testcase_dir.mkdir(exist_ok=True)
    
    # Only one test case since there's no input
    # Create input file (empty since no input needed)
    with open(testcase_dir / "input1.txt", "w") as f:
        f.write("")
    
    # Generate numbers divisible by 3 but not by 5
    result_numbers = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 != 0:
            result_numbers.append(str(i))
    
    # Create expected output file
    with open(testcase_dir / "output1.txt", "w") as f:
        f.write("\n".join(result_numbers))
    
    # Create zip file
    with zipfile.ZipFile("testcase.zip", "w") as zf:
        for file in testcase_dir.glob("*.txt"):
            zf.write(file, file.name)
    
    print(f"Created testcase for numbers divisible by 3 but not by 5 (found {len(result_numbers)} numbers)")

if __name__ == "__main__":
    create_testcase()
