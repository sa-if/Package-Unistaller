import subprocess

try:
    with open("requirements.txt", "w") as f:
        result = subprocess.run(["pip", "freeze"], stdout=f, check=True)
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

try:
    with open("requirements.txt") as f:
        packages = f.read().splitlines()

    for package in packages:
        subprocess.run(["pip", "uninstall", "-y", package], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error uninstalling package: {e}")
