from pathlib import Path

import pandas as pd

print("hello world - Jai Sri Ram")

possible_paths = [
    Path("Book1.xlsx"),
    Path("data/Book1.xlsx"),
    Path.cwd() / "Book1.xlsx",
    Path.cwd() / "data" / "Book1.xlsx",
]

excel_path = next((path for path in possible_paths if path.exists()), None)

if excel_path is None:
    print("No Excel file found. Please place Book1.xlsx in the project folder or update the path.")
else:
    read_excel = pd.read_excel(excel_path)
    print(read_excel)

# new changes to push to git