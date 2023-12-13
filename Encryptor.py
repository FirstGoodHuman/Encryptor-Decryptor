import os
try:
    os.system("py -m pip install --upgrade")
    os.system("py -m pip install cryptography")
    os.system("py -m pip install --upgrade cryptography")
    os.system("py -m pip install colorama")
    os.system("py -m pip install --upgrade colorama")
    from cryptography.fernet import Fernet
    from colorama import Fore
    print(Fore.BLUE + """
┌┌ If this is your first time entering the program, \'generate a new key\' to get started ┘┘
""")
    print(Fore.BLACK)
except:
    try:
        os.system("pip install --upgrade")
        os.system("pip install cryptography")
        os.system("pip install --upgrade cryptography")
        os.system("pip install colorama")
        os.system("pip install --upgrade colorama")
        from cryptography.fernet import Fernet
        from colorama import Fore , Back
        print(Fore.MAGENTA + """
┌┌ If this is your first time entering the program, \'generate a new key\' to get started ┘┘
""")
        print(Fore.BLACK)
    except:
        print("ERROR!")
        exit()

def CODE():
    
    q_1 = input(Fore.YELLOW + """
Do you want to :
<Generate a new KEY> [1]    (For The First Time..)
<ENCRYPT a File>     [2]
<DECRYPT a File>     [3]
<EXIT>               [\'X\']
>> """)
    print(Fore.BLACK)
    Username = os.getlogin()
    
    def KEY_GENERATOR_STEP ():
        try:
            key = Fernet.generate_key()
            with open("C:/Users/" + Username + "/Desktop/key.key" , "wb") as Key_File:
                Key_File = Key_File.write(key)
            os.system('attrib +h ' + ("C:/Users/" + Username + "/Desktop/key.key"))
        except:
            print(Fore.RED + "Key file alreday genrated!")
            print(Fore.BLUE + "If you wanna generate new key, exit and start \'Run as administrator\'...")
            print(Fore.BLACK)
            CODE()
    def ENCRYPT_STEP():
        Target_Address = input(Fore.YELLOW + "Enter The Target Location For \'Encrypt\' -> ")
        print(Fore.BLACK)
        def encrypt_codes (Target_Address):
            with open("C:/Users/" + Username + "/Desktop/key.key" , "rb") as Key_File:
                Key_File = Key_File.read()
            f = Fernet(Key_File)
            with open(Target_Address , "rb") as Orginal_File:
                Orginal_File = Orginal_File.read()
            Encrypt = f.encrypt(Orginal_File)
            with open(Target_Address , "wb") as Encrypted_File:
                Encrypted_File = Encrypted_File.write(Encrypt)
        for Root,Dirs,Files in os.walk(Target_Address):
            for File in Files:
                encrypt_codes(os.path.join(Root , File))

    def DECRYPT_STEP():
        try:
            Target_Address = input(Fore.YELLOW + "Enter The Target Location For \'Dncrypt\' -> ")
            print(Fore.BLACK)
            def decrypt_codes (Target_Address):       
                with open("C:/Users/" + Username + "/Desktop/key.key" , "rb") as Key_File:
                    Key_File = Key_File.read()
                f = Fernet(Key_File)
                with open(Target_Address , "rb") as Decrypted_File:
                    Decrypted_File = Decrypted_File.read()
                Decript = f.decrypt(Decrypted_File)
                with open(Target_Address , "wb") as Orginal_File:
                    Orginal_File = Orginal_File.write(Decript)
            for Root,Dirs,Files in os.walk(Target_Address):
                for File in Files:
                    decrypt_codes(os.path.join(Root , File))
            decrypt_codes(Target_Address)
        except PermissionError:
            pass
        except:
            print(Fore.RED + "Error in decrypt process!")
            print(Fore.BLACK)
            exit()
        
    if (q_1 == "1" or q_1 == "2" or q_1 == "3" or q_1 == "X" or q_1 == "x"):
        if (q_1 == "1"):
            KEY_GENERATOR_STEP()
            print(Fore.GREEN + "Key was generated.")
            print(Fore.BLACK)
        elif(q_1 == "2"):
            ENCRYPT_STEP()
            print(Fore.GREEN + "File/Folder was encrypted.")
            print(Fore.BLACK)
        elif(q_1 == "3"):
            DECRYPT_STEP()
            print(Fore.GREEN + "File/Folder was decrypted.")
            print(Fore.BLACK)
        elif(q_1 == "x" or q_1 == "X"):
            exit()
    else:
        print(Fore.RED + "PLS enter a valid option! (1 or 2 or 3 or \'X\')")
        print(Fore.BLACK)
        CODE()
    

CODE()
