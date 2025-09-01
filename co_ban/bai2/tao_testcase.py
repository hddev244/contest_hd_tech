import zipfile
from pathlib import Path

# Test cases input and output
inputs = [
    "10\n5\n2",
    "15\n3\n4",
    "20\n8\n5",
    "12\n6\n3",
    "18\n9\n2"
]

# Tính toán outputs
outputs = []
for inp in inputs:
    lines = inp.split('\n')
    a = int(lines[0])
    b = int(lines[1])
    c = int(lines[2])

    tong = a + b + c
    hieu = a - b - c
    tich = a * b * c
    thuong = a / (b * c)

    # Format thương (loại bỏ .0 nếu là số nguyên)
    thuong_str = f"{thuong:.2f}".rstrip('0').rstrip('.')

    outputs.append(f"Tổng: {tong}\nHiệu: {hieu}\nTích: {tich}\nThương: {thuong_str}")

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
