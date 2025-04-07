from stats import generate_report 
import sys

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	file = sys.argv[1]
	report = generate_report(file)
	print(report)

main()
