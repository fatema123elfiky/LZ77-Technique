from numpy.random.mtrand import Sequence

class LZ77:
    """That class is responsible for compressing and decompressing using data LZ77."""

    def __init__(self):
        """Just default constructor"""
        self.size = 11
        self.SearchWindow = ""
        self.LookAheadWindow = []

    def stringify(self, Tags):
        """Stringify is taking list of tuples and print them in the way of tags and return a string of tags
        @:parameter list of tuples of tags
        @:return string of tags
        """
        stringifiedTags = ""
        for Tag in Tags:
            stringifiedTags += f"<{Tag[0]},{Tag[1]},{Tag[2]}> "
        return stringifiedTags

    def compressor(self):
        """Compress the input using LZ77 algorithm.
        @:parameter empty
        @:return list of tuples of tags
        """
        data = input("Enter data to be compressed: ")
        compressedData = []

        if len(data) < self.size:
            self.size = len(data)

        leftAhead, rightAhead = 0, self.size
        leftSearch, rightSearch = 0, 0
        self.LookAheadWindow = data[leftAhead: rightAhead]
        self.SearchWindow = data[leftSearch: rightSearch]

        while (leftAhead < len(data)) and len(self.LookAheadWindow):

            longest = 0
            posOfLongest = 0

            # Try to go back to every pos in the search window
            for pos in range(1, len(self.SearchWindow)+1):

                currentIdx = len(self.SearchWindow) - pos

                length = 0
                while length < len(self.LookAheadWindow):

                    if currentIdx + length < len(self.SearchWindow):
                        c = self.SearchWindow[currentIdx + length]
                    else:
                        c = self.LookAheadWindow[length - (len(self.SearchWindow) - currentIdx)]

                    if c != self.LookAheadWindow[length]:
                        break
                    length += 1

                if length > longest:
                    longest = length
                    posOfLongest = pos

            nextSymbol = ""
            if longest < len(self.LookAheadWindow):
                nextSymbol = self.LookAheadWindow[longest]

            if longest > 0:
                tag = tuple((posOfLongest, longest, nextSymbol))
                leftAhead += longest + 1
            else:
                tag = tuple((0, 0, nextSymbol))
                leftAhead += 1

            compressedData.append(tag)

            # Update the Search and Look-Ahead buffers
            rightAhead = min(len(data), leftAhead + self.size)
            rightSearch = leftAhead
            leftSearch = max(0, rightSearch - self.size)

            self.SearchWindow = data[leftSearch:rightSearch]
            self.LookAheadWindow = data[leftAhead:rightAhead]

        return compressedData

    def decompress(self):
        """Decompress the input using LZ77 algorithm.
        @:parameter empty
        @:return original text
        """
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
