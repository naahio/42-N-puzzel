from parser import file_parser
import sys, getopt


if __name__ == "__main__":
    filename = sys.argv[1]
    # print(sys.argv[1])
    file_parser(filename)
