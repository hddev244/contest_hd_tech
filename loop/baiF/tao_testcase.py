import zipfile
from pathlib import Path

inputs = ["5", "3", "4", "1", "6"]
outputs = ["120", "6", "24", "1", "720"]

tc_dir = Path("testcase")
tc_dir.mkdir(exist_ok=True)

for i in range(len(inputs)):
    (tc_dir / f"{i}.in").write_text(inputs[i] + "\n", encoding="utf-8")
    (tc_dir / f"{i}.out").write_text(outputs[i] + "\n", encoding="utf-8")

zip_path = Path("testcase.zip")
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file in tc_dir.iterdir():
        zipf.write(file, file.name)

print(f"Đã tạo file zip: {zip_path.absolute()}")
print(f"Số lượng test case: {len(inputs)}")
