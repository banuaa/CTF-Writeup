import os
import exiftool

for i in range(0, 1000):
	number = 1000 - i
	ef = exiftool.ExifToolHelper()
	file = f"matreshka_{number}.zip"
	passwd = ef.get_tags(file, "Comment")[0]['File:Comment'].split()[-1]
	os.system(f"7z x {file} -p{passwd}")