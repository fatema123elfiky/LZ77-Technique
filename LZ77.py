class LZ77:
    """That class is responsible for compressing and decompressing using data LZ77."""
    def __init__(self,input):
        self.input = input
    def compress(self):
        """Compress the input using LZ77 algorithm."""

    def decompress(self):
        """Decompress the input using LZ77 algorithm."""
        user_input = input("Enter compressed triples like <0,0,A> <0,0,B> <2,9,>\n=> ")
    
        compressed_data = []
        for part in user_input.split():
            part = part.strip("<>")
            pos, length, char = part.split(",")
            pos = int(pos)
            length = int(length)
            compressed_data.append((pos, length, char))
    
        output = ""
        for position, length, next_char in compressed_data:
            if position == 0 and length == 0:
                output += next_char
            else:
                start = len(output) - position
                for i in range(length):
                    output += output[start + i]
                output += next_char

        print("\nDecompressed text:", output)
        return output
        

