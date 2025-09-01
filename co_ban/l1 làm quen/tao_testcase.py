import zipfile
from pathlib import Path

# Tạo thư mục chứa file test case
tc_dir = Path("testcase_1")
tc_dir.mkdir(exist_ok=True)

# Tạo file 1.in
(tc_dir / "1.in").write_text("An\n13\nchơi bóng đá\n", encoding="utf-8")

# Tạo file 1.out
(tc_dir / "1.out").write_text(
    "Xin chào, mình tên là An, năm nay 13 tuổi.\nMình thích chơi bóng đá.\n",
    encoding="utf-8"
)

# Nén thành file zip
zip_path = Path("testcase_1.zip")
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file in tc_dir.iterdir():
        zipf.write(file, file.name)

print(f"Đã tạo file zip: {zip_path.absolute()}")
