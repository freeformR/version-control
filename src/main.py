import os
from datetime import datetime

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

file_path = os.path.join("/repo/version-control/output", "version.md")
with open(file_path, "w") as file:
	file.write(current_time)
