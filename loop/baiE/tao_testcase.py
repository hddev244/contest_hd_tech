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
    
    # Create expected output file
    odd_numbers = [str(i) for i in range(1, 20, 2)]
    with open(testcase_dir / "output1.txt", "w") as f:
        f.write("\n".join(odd_numbers))
    
    # Create zip file
    with zipfile.ZipFile("testcase.zip", "w") as zf:
        for file in testcase_dir.glob("*.txt"):
            zf.write(file, file.name)
    
    print("Created testcase for odd numbers 1-19")

if __name__ == "__main__":
    create_testcase()
