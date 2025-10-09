import LZ77 as cp

while True:
    print('Welcome to LZ77\n')

    choice=input("What would you like to do ?\n1.Compress\n2.Decompress\n3.Exit\n")

    compressor = cp.LZ77()

    if choice=='1':
        Tags=compressor.Compressor()
        print(compressor.Stringify(Tags))
    elif choice=='2' :
        compressor.decompress()
    elif choice=='3' :
        print('Thanks for using LZ77')
        break
    else:
        print('Invalid choice')

