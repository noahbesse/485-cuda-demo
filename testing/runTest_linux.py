import subprocess
import sys


def main():
    n = len(sys.argv)

    if (n != 4):
        print("Usage: python "+ sys.argv[0] +" <inputFile> <rows> <char to search for>")
        return
    inputFile = sys.argv[1]
    rows = sys.argv[2]
    character = sys.argv[3]

    subprocess.run(["./cpuNumberCounting", inputFile, rows, character])
    print("\n")
    subprocess.run(["./gpuNumberCounting", inputFile, rows, character])

if __name__ == "__main__":
    main()