import argparse
from program import Program

print("\nCompression/Descompression Program")
print("=================================================================\n")

ap = argparse.ArgumentParser()

ap.add_argument('-r', '--resize', required=True,
                help='Float value to resize the image')
ap.add_argument('-s', '--show', required=False,
                help='Show the two images side by side after descompress')
ap.add_argument('-m', '--method', required=True,
                help='Insert "c" to compress or "d" to descompress')

args = vars(ap.parse_args())

file = args.get("file", None)
method = args.get("method", None)
perc = float(args.get('resize', None))/100
show = args.get('show', False)

program = Program(fator=perc)

if method == 'c':
    program.compress()
elif method == 'd':
    program.descompress(show)
else:
    print('Invalid working method')

print()
