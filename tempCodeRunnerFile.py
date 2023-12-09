message = input("Enter a message to be hashed by SHA-1 : ")

SHA_1_result = SHA_1_algorithm(message)

print (f"SHA-1 Result for message {message} is : {SHA_1_result} With Lenth = {len(SHA_1_result)}")