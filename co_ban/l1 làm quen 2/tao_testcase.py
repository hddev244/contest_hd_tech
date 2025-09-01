import zipfile
from pathlib import Path

# Test cases input and output
inputs = [
    "Mai, 14, Huế, 0123456789",
    "An, 20, Hà Nội, 0987654321",
    "Lan, 18, Đà Nẵng, 0911222333",
    "Bình, 25, TP.HCM, 0909090909",
    "Hải, 30, Cần Thơ, 0933555777"
]

outputs = [
    "Xin chào, mình là Mai, năm nay 14 tuổi.\nMình ở Huế. Số điện thoại của mình là: 0123456789.",
    "Xin chào, mình là An, năm nay 20 tuổi.\nMình ở Hà Nội. Số điện thoại của mình là: 0987654321.",
    "Xin chào, mình là Lan, năm nay 18 tuổi.\nMình ở Đà Nẵng. Số điện thoại của mình là: 0911222333.",
    "Xin chào, mình là Bình, năm nay 25 tuổi.\nMình ở TP.HCM. Số điện thoại của mình là: 0909090909.",
    "Xin chào, mình là Hải, năm nay 30 tuổi.\nMình ở Cần Thơ. Số điện thoại của mình là: 0933555777."
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
