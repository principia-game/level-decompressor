import sys
import zlib
from plvl import Plvl

def main(input_file):
	level = Plvl.from_file(input_file)
	buffer = level.level_buffer
	decomp_buffer = zlib.decompress(buffer)

	with open("decompressed_buffer", "wb") as f:
		f.write(decomp_buffer)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("[WARNING] No file chosen, will use level.plvl in working directory if it exists.")
		main("level.plvl")
	else:
		main(sys.argv[1])
