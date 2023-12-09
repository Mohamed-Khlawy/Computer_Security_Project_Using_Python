############################################### SOHA GAMAL ############################################
from math import fmod
def SHA_1_algorithm(message):
    message_Binary = ""

    #Seed Values (Constant in algorithm)
    a = h0 = 0x67452301
    b = h1 = 0xEFCDAB89
    c = h2 = 0x98BADCFE
    d = h3 = 0x10325476
    e = h4 = 0xC3D2E1F0
    #Task1:Appending Padding Bits 
    #First : convert MSG TO BINARY
    for i in range(len(message)):
        message_Binary+='{0:08b}'.format(ord(message[i]))

    temp_msg = message_Binary = message_Binary + "1"
    message_length = len(message_Binary)
    
    # WE HAVE 2 CASES
    
    if (message_length<448):
        num_zeros = 448- message_length
        for i in range (num_zeros):
            message_Binary+='0'
    
    else:
        num_zeros=448 - int(fmod(message_length, 512))
        for i in range (num_zeros):
            message_Binary+='0'
                    
    
    # Task2: Appending Length of Message
    message_Binary += '{0:064b}'.format(len(temp_msg)-1) # Convert the lenght in format 64 bite 
    # print(message_Binary)
    
    
    #Editing by ENG/ Mohamed
    def split_into_chunks(sequence, chunk_size):
        return [sequence[i:i+chunk_size] for i in range(0, len(sequence), chunk_size)]
    
    def Rotate(bits, shift_value):
        return ((bits << shift_value) | (bits >> (32 - shift_value))) & 0xffffffff
    
    # Generate 80 words
    for chunk in split_into_chunks(message_Binary, 512):
        words = split_into_chunks(chunk, 32)
        w = [0]*80

        #Generate First 16 words
        for n in range(0, 16):
            w[n] = int(words[n], 2)
        #Generate from 16 : 80 words (64 words)
        for i in range(16, 80):
            w[i] = Rotate((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 1)& 0xffffffff
            
        # Preparing Processing Functions
        #we divid it into 4 group (32 for each group)
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

            temp = Rotate(a, 5) + f + e + k + w[i] & 0xffffffff
            e = d
            d = c
            c = Rotate(b, 30)
            b = a
            a = temp

        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff

        

    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

# Calling SHA-1 Function
# msg = "Kasper Team"
# print (SHA_1_algorithm(msg))

