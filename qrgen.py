import pyqrcode


def generate(y , z= "code.png"):
     url = pyqrcode.create(y)
     url.png(z+".png" ,scale = 8)
     print("successefully saved")

if __name__ == "__main__":
    print("Welcome TO QR CODE GENERATOR\n")
    while True:
        print("1 for generating new qrcode \n2 for quiting\n\n")
        x = input("> ")
        if(int(x) ==1):
            y = input("enter the text for generating qrcode ex www.google.com\n")
            z = input("enter name of file\n")
            generate(y,z)
            for i in range(0,7):
                print("\n\n")
        elif (int(x) == 2):
            print("quiting......")
            break
        
        
