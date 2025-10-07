class LZ77:
    """That class is responsible for compressing and decompressing using data LZ77."""
    def __init__(self,input):
        self.input = input
    def compress(self):
        """Compress the input using LZ77 algorithm."""

    def decompress(self, compressed_data):
        """Decompress the input using LZ77 algorithm."""
        output = ""

        for position, length, next_char in compressed_data:
            if position == 0 and length == 0:
                """ Just a literal character"""
                output += next_char
            else:
                """ Copy substring from decompressed data"""
                start = len(output) - position
                for i in range(length):
                    output += output[start + i]
                output += next_char

        return output

    def menu(self):
        """Display menu for user to choose compress or decompress."""
        choice = input("Enter 'c' to compress or 'd' to decompress: ").lower()


        if choice == 'd':
            print("Enter compressed triples in format: <position,length,next character> separated by spaces.")
            user_input = input("Example: <0,0,A> <0,0,B> <2,9,>\n=> ")

            compressed_data = []
            for part in user_input.split():
                part = part.strip("<>")
                position, length, char = part.split(",")
                position = int(position)
                length = int(length)
                compressed_data.append((position, length, char))
            
            decompressed = self.decompress(compressed_data)
            print("\nDecompressed text:", decompressed)
        
        #elif choice == 'c;

        else:
            print("Invalid choice! Please enter 'c' or 'd'.")
