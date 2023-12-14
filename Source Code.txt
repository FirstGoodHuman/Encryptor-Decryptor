import os

try:
    os.system("py -m pip install --upgrade")
    os.system("py -m pip install cryptography")
    os.system("py -m pip install --upgrade cryptography")
    os.system("py -m pip install colorama")
    os.system("py -m pip install --upgrade colorama")
    from cryptography.fernet import Fernet
    from colorama import Fore
    print(Fore.MAGENTA + """
┌┌ If this is your first time entering the program, \'generate a new key\' to get started ┘┘
""")
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
    except:
        print(Fore.RED + "ERROR!")
        exit()
        
try:
    os.system("cls")
except:
    try:
        os.system("clear")
    except:
        pass
##################################################
def CODE():
    q_1 = input(Fore.YELLOW + """
Do you want to :
<Generate a new KEY> [1]    (For The First Time...)
<Encrypt a File>     [2]
<Decrypt a File>     [3]
>> """)
    Username = os.getlogin()
    

    def KEY_GENERATOR_STEP ():
        try:
            Template_Key_File = open("C:/Users/" + Username + "/Desktop/key.key")
            Template_Key_File.close()
            Remove_Use_Key = input(Fore.YELLOW + """
You have a file named \"key.key\" in this path ==> \"C:/Users/"{}"/Desktop/key.key\"
Do you want to remove it or use it? ([R]emove , [U]se):
>> """.format(Username))
            if (Remove_Use_Key == "R" or Remove_Use_Key == "r"):
                os.system("del /s /a \"C:\\Users\\mrami\\Desktop\\key.key\" ".format(Username))
                print(Fore.RED + "key.key was deleted!")
            if (Remove_Use_Key == "U" or Remove_Use_Key == "u"):
                pass
        except FileNotFoundError:
            pass
        try:
            key = Fernet.generate_key()
            with open("C:/Users/" + Username + "/Desktop/key.key" , "wb") as Key_File:
                Key_File = Key_File.write(key)
            os.system('attrib +h ' + ("C:/Users/" + Username + "/Desktop/key.key"))
        except:
            print(Fore.RED + "Key file alreday genrated!")
            print(Fore.BLUE + "If you wanna generate new key, exit and start \'Run as administrator\'...")
            CODE()


    def ENCRYPT_STEP():
        Target_Address = input(Fore.YELLOW + "Enter The Target Location For \'Encrypt\' -> ")
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
            Target_Address = input(Fore.YELLOW + "Enter The Target Location For \'Decrypt\' -> ")
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
            exit()


    if (q_1 == "1" or q_1 == "2" or q_1 == "3"):
        if (q_1 == "1"):
            KEY_GENERATOR_STEP()
            print(Fore.GREEN + "Key was generated.")
            CODE()
        elif(q_1 == "2"):
            ENCRYPT_STEP()
            print(Fore.GREEN + "File/Folder was encrypted.")
            CODE()
        elif(q_1 == "3"):
            DECRYPT_STEP()
            print(Fore.GREEN + "File/Folder was decrypted.")
            CODE()
    else:
        print(Fore.RED + "PLS enter a valid option! (1 or 2 or 3)")
        CODE()
    

CODE()
