import zipfile
from pathlib import Path

# Test cases input and output
inputs = [
    "3 2",
    "4 5",
    "1 1",
    "2 1",
    "0 5"
]

outputs = [
    "Tổng lớn hơn",
    "Tích lớn hơn hoặc bằng",
    "Tích lớn hơn hoặc bằng",
    "Tổng lớn hơn",
    "Tổng lớn hơn"
]

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
