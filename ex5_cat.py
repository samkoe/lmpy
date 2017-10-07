# # ex5_cat.py

# import argparse

# parser = argparse.ArgumentParser()

# parser.add_argument("-n", "--newfile", help="concatenate to new file", action="store_true")

# parser.add_argument("files", metavar="F", help="filenames", nargs="+")
# # parser.add_argument("endfile", help="name of destination file")


# args = parser.parse_args()

# print(">>> parsed args: ", args)

# end_file = ""

# for filename in args.files:
#     in_file = open(filename, 'r')
#     # in_file = first_file.read()
#     # end_file = end_file + in_file

#     if args.newfile:
#         endfile = open(args.endfile, 'w')
#         end_file = file_1 + file_2

#         endfile.write(end_file)
#         endfile.close()

#     else:
#         print(in_file.read())

#     in_file.close()

import argparse
parser = argparse.ArgumentParser()

parser.add_argument('files', metavar='F', type=str, nargs='+')
parser.add_argument('-n', '--numbers', action='store_true',
        help='Print line numbers')

args = parser.parse_args()

print(">>> parsed args: ", args)

line_number = 1
for in_file_name in args.files:
    in_file = open(in_file_name)
    if args.numbers:
        for line in in_file.readlines():
            print(f"\t{line_number}\t{line}", end="")
            line_number += 1
    else:
        print(in_file.read())