# Code Link: https://codereview.stackexchange.com/questions/37648/python-implementation-of-sha1
#----------------------------------------------------------------------------------------------

def SHA_1_algorithm(message):
    bytes = ""

    #Seed Values
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    for i in range(len(message)):
        bytes+='{0:08b}'.format(ord(message[i]))

    bits = bytes + "1"

    padding_bits = bits

    # Add pading bits until length equal to 448 % 512
    while len(padding_bits) % 512 != 448:
        padding_bits += "0"

    # Append original length
    padding_bits += '{0:064b}'.format(len(bits)-1)

    def split_into_chunks(sequence, chunk_size):
        return [sequence[i:i+chunk_size] for i in range(0, len(sequence), chunk_size)]
    
    def circular_left_shift(bits, shift_value):
        return ((bits << shift_value) | (bits >> (32 - shift_value))) & 0xffffffff
    
    for chunk in split_into_chunks(padding_bits, 512):
        words = split_into_chunks(chunk, 32)
        w = [0]*80

        # First 16 word
        for n in range(0, 16):
            w[n] = int(words[n], 2)
        # Other words (64 words)
        for i in range(16, 80):
            w[i] = circular_left_shift((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 1)

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        # Preparing Processing Functions
        for i in range(0, 80):
            if 0 <= i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d) 
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = circular_left_shift(a, 5) + f + e + k + w[i] & 0xffffffff
            e = d
            d = c
            c = circular_left_shift(b, 30)
            b = a
            a = temp

        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff

    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

# Calling SHA-1 Function
# message = input("Enter a message to be hashed by SHA-1 : ")

# SHA_1_result = SHA_1_algorithm(message)

# print (f"SHA-1 Result for message {message} is : {SHA_1_result} With Lenth = {len(SHA_1_result)}")