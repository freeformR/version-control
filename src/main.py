import os
import time

file_path = os.path.join("/repo/version-control/output", "version.md")
with open(file_path, "w") as file:
	file.write(f"{time.time()}")
