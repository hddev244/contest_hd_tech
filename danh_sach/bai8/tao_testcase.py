import zipfile
from pathlib import Path

# Test cases input and output
inputs = [
    "3\n10\n20\n30",
    "5\n1\n2\n3\n4\n5",
    "4\n100\n200\n300\n400",
    "2\n7\n9",
    "6\n11\n22\n33\n44\n55\n66"
]

# Tính toán outputs
outputs = []
for inp in inputs:
    lines = inp.split('\n')
    n = int(lines[0])
    numbers = []
    for i in range(1, n + 1):
        numbers.append(lines[i])
    outputs.append(' '.join(numbers))

# Tạo thư mục chứa file test case
tc_dir = Path("testcase")
tc_dir.mkdir(exist_ok=True)

# Tạo các file test case từ danh sách inputs và outputs
for i in range(len(inputs)):
    # Tạo file i.in
    (tc_dir / f"{i}.in").write_text(inputs[i] + "\n", encoding="utf-8")

    # Tạo file i.out
    (tc_dir / f"{i}.out").write_text(outputs[i] + "\n", encoding="utf-8")

# Nén thành file zip
zip_path = Path("testcase.zip")
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file in tc_dir.iterdir():
        zipf.write(file, file.name)

print(f"Đã tạo file zip: {zip_path.absolute()}")
print(f"Số lượng test case: {len(inputs)}")
