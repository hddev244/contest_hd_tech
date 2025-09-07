import zipfile
from pathlib import Path

inputs = [""] * 5
outputs = [
    "5 x 1 = 5\n5 x 2 = 10\n5 x 3 = 15\n5 x 4 = 20\n5 x 5 = 25\n5 x 6 = 30\n5 x 7 = 35\n5 x 8 = 40\n5 x 9 = 45\n5 x 10 = 50"
] * 5

tc_dir = Path("testcase")
tc_dir.mkdir(exist_ok=True)

for i in range(len(inputs)):
    (tc_dir / f"{i}.in").write_text("", encoding="utf-8")
    (tc_dir / f"{i}.out").write_text(outputs[i] + "\n", encoding="utf-8")

zip_path = Path("testcase.zip")
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file in tc_dir.iterdir():
        zipf.write(file, file.name)

print(f"Đã tạo file zip: {zip_path.absolute()}")
print(f"Số lượng test case: {len(inputs)}")
