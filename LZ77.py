class LZ77:
    """That class is responsible for compressing and decompressing using data LZ77."""
    def __init__(self,input):
        self.input = input
    def compress(self):
        """Compress the input using LZ77 algorithm."""

    def decompress(self):
        """Decompress the input using LZ77 algorithm."""
        output = ""

        for position, length, next_char in input:
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
        

