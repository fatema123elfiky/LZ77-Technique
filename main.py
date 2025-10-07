import LZ77 as cp

while True:
    data=input('Welcome to LZ77\n\nCould you enter the text : ')
    compressor=cp.LZ77(data)

    choice=input("What would you like to do ?\n1.Compress\n2.decompress\n3.Exit")

    if choice=='1':
        compressor.compress()
    elif choice=='2' :
        compressor.decompress()
    elif choice=='3' :
        print('Thanks for using LZ77')
        break
    else:
        print('Invalid choice')

