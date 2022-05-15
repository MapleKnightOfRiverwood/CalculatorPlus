import os.path


class fileEncryptor:

    @staticmethod
    def encrypt(fileLocation, destination):
        if os.path.exists(fileLocation):
            file = open(fileLocation, "rb")
            fileContents = file.read()  # fileContents is a byte string
            file.close()

            btAr = bytearray(fileContents)  # Byte string needs to be changed to byte array to manipulate

            length = len(btAr)
            n = 0
            while n < length:
                increment = 6
                if btAr[n] <= 249:
                    btAr[n] = btAr[n] + increment
                elif 249 < btAr[n] <= 255:
                    btAr[n] = btAr[n] - 250
                n = n + 1
            btString = bytes(btAr)

            encryptedFile = open(destination, "wb")
            encryptedFile.write(btString)
            encryptedFile.close()
        else:
            print("File does not exist")

    @staticmethod
    def decrypt(fileLocation, destination):
        if os.path.exists(fileLocation):
            file = open(fileLocation, "rb")
            fileContents = file.read()
            file.close()

            btAr = bytearray(fileContents)

            length = len(btAr)
            n = 0
            while n < length:
                increment = 6
                if 5 < btAr[n] <= 255:
                    btAr[n] = btAr[n] - 6
                elif btAr[n] <= 5:
                    btAr[n] = btAr[n] + 250
                n = n + 1
            btString = bytes(btAr)

            decryptedFile = open(destination, "wb")
            decryptedFile.write(btString)
            decryptedFile.close()
        else:
            print("File does not exist")