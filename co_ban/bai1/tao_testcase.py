import zipfile
from pathlib import Path

# Test cases input and output
inputs = [
    "An\n18",
    "Mai\n22",
    "Bình\n25",
    "Lan\n19",
    "Hải\n30"
]

outputs = [
    "Xin chào An, bạn 18 tuổi.",
    "Xin chào Mai, bạn 22 tuổi.",
    "Xin chào Bình, bạn 25 tuổi.",
    "Xin chào Lan, bạn 19 tuổi.",
    "Xin chào Hải, bạn 30 tuổi."
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
