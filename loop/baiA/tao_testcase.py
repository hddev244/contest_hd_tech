import zipfile
from pathlib import Path

# Bài này không có input, chỉ có output cố định
inputs = [""] * 5  # 5 test case giống nhau

outputs = [
    "1\n2\n3\n4\n5\n6\n7\n8\n9\n10",
    "1\n2\n3\n4\n5\n6\n7\n8\n9\n10", 
    "1\n2\n3\n4\n5\n6\n7\n8\n9\n10",
    "1\n2\n3\n4\n5\n6\n7\n8\n9\n10",
    "1\n2\n3\n4\n5\n6\n7\n8\n9\n10"
]

# Tạo thư mục chứa file test case
tc_dir = Path("testcase")
tc_dir.mkdir(exist_ok=True)

# Tạo các file test case từ danh sách inputs và outputs
for i in range(len(inputs)):
    # Tạo file i.in (rỗng)
    (tc_dir / f"{i}.in").write_text("", encoding="utf-8")

    # Tạo file i.out
    (tc_dir / f"{i}.out").write_text(outputs[i] + "\n", encoding="utf-8")

# Nén thành file zip
zip_path = Path("testcase.zip")
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file in tc_dir.iterdir():
        zipf.write(file, file.name)

print(f"Đã tạo file zip: {zip_path.absolute()}")
print(f"Số lượng test case: {len(inputs)}")
