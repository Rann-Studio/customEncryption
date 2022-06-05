import os, sys, string, random

stdKey = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def generateKey():
    characters = string.ascii_letters + string.digits + '+/'
    key = ''.join(random.sample(characters, len(characters)))
    return key

def encrypt(inpStr, key):
    result = inpStr.translate(str.maketrans(key, stdKey))
    return result
    
def decrypt(inpStr, key):
    result = inpStr.translate(str.maketrans(stdKey, key))
    return result

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')
    
if __name__ == '__main__':
    clearConsole()
    menu = input("Menu : \n1. Encrypt \n2. Decrypt \nSelect : ")
    
    if menu == 1 or menu == '1':
        clearConsole()
        submenu = input("Menu : \n1. Encrypt file \n2. Encrypt string \nSelect : ")
        
        if submenu == 1 or submenu == '1':
            clearConsole()
            inpFile = input("Input file name : ")
            if not os.path.isfile(inpFile):
                sys.exit("File not found")
                
            outFile = input("Output file name : ")
            key = generateKey()
            
            with open(inpFile, 'r') as f:
                data = f.read()
                
            with open(outFile, 'w') as f:
                f.write(f"# Decrypt Key : {key}\n\n{encrypt(data, key)}")
                
            print("Encrypt success")
                
        if submenu == 2 or submenu == '2':
            clearConsole()
            inpStr = input("String to encrypt : ")
            key = generateKey()
            print(f"# Decrypt Key : {key}\n\nOutput : {encrypt(inpStr, key)}")
            
    if menu == 2 or menu == '2':
        clearConsole()
        submenu = input("Menu : \n1. Decrypt file \n2. Decrypt string \nSelect : ")
        
        if submenu == 1 or submenu == '1':
            clearConsole()
            inpFile = input("Input file name : ")
            if not os.path.isfile(inpFile):
                sys.exit("File not found")
                
            outFile = input("Output file name : ")
            key = input("Decrypt key : ")
            
            with open(inpFile, 'r') as f:
                data = f.read()
                for line in data.splitlines():
                    if line.startswith('# Decrypt Key : '):
                        data = data.replace(line, '')
                
            with open(outFile, 'w') as f:
                f.write(decrypt(data, key))
                
            print("Decrypt success")
            
        if submenu == 2 or submenu == '2':
            clearConsole()
            inpStr = input("String to decrypt : ")
            key = input("Decrypt key : ")
            print(f"Output : {decrypt(inpStr, key)}")