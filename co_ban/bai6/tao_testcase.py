import zipfile
from pathlib import Path

# Test cases input and output
inputs = [
    "An\n2005",
    "Mai\n1998",
    "Bình\n2000",
    "Lan\n1995",
    "Hải\n2003"
]

# Tính toán outputs
outputs = []
for inp in inputs:
    lines = inp.split('\n')
    ten = lines[0]
    nam_sinh = int(lines[1])
    tuoi = 2025 - nam_sinh
    outputs.append(f"Xin chào {ten}, bạn {tuoi} tuổi.")

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
