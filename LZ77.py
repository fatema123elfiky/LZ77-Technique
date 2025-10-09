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
        CompressedData = []

        if len(data) < self.size:
            self.size = len(data)

        LeftA, RightA = 0, self.size
        LeftS, RightS = 0, 0
        self.LookAheadWindow = data[LeftA:RightA]
        self.SearchWindow = data[LeftS:RightS]

        Sequence = ""
        Sequence += (self.LookAheadWindow[0])

        while (LeftA < len(data)) and len(self.LookAheadWindow):

            startOfSequence = LeftA
            found = False

            while (Sequence in self.SearchWindow) and (LeftA < RightA):
                found = True
                LeftA += 1
                if RightA < len(data):
                    RightA += 1
                if LeftA < RightA:
                    Sequence += (self.LookAheadWindow[LeftA - startOfSequence])

            # LookAhead updates
            LeftA += 1
            if RightA < len(data):
                RightA += 1
            if LeftA < RightA:
                self.LookAheadWindow = data[LeftA:RightA]
            else:
                self.LookAheadWindow = []

            # For loop to get the position and add to tags
            NextSymbol = Sequence[-1]
            Sequence = Sequence[:-1]

            if found:
                Pos = -1
                for idx in range(LeftS, RightS):
                    if Sequence == self.SearchWindow[idx:(idx + len(Sequence))]:
                        Pos = max(idx, Pos)

                tag = tuple((startOfSequence - Pos, len(Sequence), NextSymbol))
            else:
                tag = tuple((0, 0, NextSymbol))
            CompressedData.append(tag)

            # Update the new sequence
            Sequence = ""
            if len(self.LookAheadWindow):
                Sequence += self.LookAheadWindow[0]
            else:
                break

            # Part of changing search buffer
            if LeftA - LeftS <= len(data):
                RightS = LeftA
            else:
                RightS = LeftA
                LeftS = RightS - self.size

            self.SearchWindow = data[LeftS:RightS]

        return CompressedData

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
