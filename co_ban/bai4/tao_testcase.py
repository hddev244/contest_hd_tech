import zipfile
from pathlib import Path

# Test cases input and output
inputs = [
    "10\n5",
    "7.5\n3.2",
    "12\n8",
    "6.8\n4.5",
    "15\n9"
]

# Tính toán outputs
outputs = []
for inp in inputs:
    lines = inp.split('\n')
    chieu_dai = float(lines[0])
    chieu_rong = float(lines[1])
    chu_vi = 2 * (chieu_dai + chieu_rong)
    dien_tich = chieu_dai * chieu_rong

    # Format số (loại bỏ .0 nếu là số nguyên)
    chu_vi_str = f"{chu_vi:.1f}".rstrip('0').rstrip('.')
    dien_tich_str = f"{dien_tich:.1f}".rstrip('0').rstrip('.')

    outputs.append(f"Chu vi: {chu_vi_str}\nDiện tích: {dien_tich_str}")

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
