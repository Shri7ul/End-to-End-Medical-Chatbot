import os

# Creating directory
os.makedirs("src", exist_ok=True)

# Creating files
files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "store_index.py"
]

for file in files:
    with open(file, "w") as f:
        pass  # just create empty file

print("Directory and files created successfully!")