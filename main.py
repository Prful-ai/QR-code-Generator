import os
import qrcode as qr
OUTPUT_FOLDER="output"
def ensure_output_folder():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
def generate_qr():
    text=input("Enter text or URL: ").strip()
    if not text:
        print("Input cannot be empty")
        return
    filename=input("Enter filename : ").strip()
    if not filename:
        filename="qrcode"
    filename=filename + ".png"
    filepath=os.path.join(OUTPUT_FOLDER,filename)

    qr_code = qr.QRCode(
    version=1,
    box_size=10,
    border=4,
    error_correction=qr.constants.ERROR_CORRECT_H
    )
    qr_code.add_data(text)
    qr_code.make(fit=True)
    img = qr_code.make_image(fill_color="black", back_color="white")
    img.save(filepath)

    print(f"QR code saved at: {os.path.abspath(filepath)}")
def view_output_files():
    print("\nGenerated  QR codes: ")
    if not os.path.exists(OUTPUT_FOLDER):
        print("no files found")
    files=os.listdir(OUTPUT_FOLDER)
    if not files:
        print("No qr generated")
        return
    
    for f in files:
        print(" -",f)

def main():
    ensure_output_folder()
    while True:
        choice=input("Enter your chice (1-3): ").strip()
        if choice=="1":
            generate_qr()
        elif choice=="2":
            view_output_files()
        elif choice=="3":
            print("exiting program")
            break
if __name__=="__main__":
    main()

