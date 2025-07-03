# Project_ASCII: BINARY ASCII IMAGE GENERATOR

Welcome to Project_ASCII, A simple Python program that allows users to convert an image into binary (1s and 0s) art, display it in the terminal, Exportable to Text and PDF format


## 4 Pillars of OOP
We will now discuss the presence of each Pillars of OOP in this section

Each will have their own description 

### ENCAPSULATION

Encapsulation is the bundling related data into a structured unit, along with the methods used to work with that data, we can see an example of its presence in this section of the code block

```Python

class BinaryArtGenerator:
    def __init__(self, creator_name: str):
        self.creator_name = creator_name
        self.image_path = ""
        self.binary_art = ""
        self.output_directory = ""
        self.base_filename = ""

    def display_header(self):
        print(Fore.CYAN + "\n" + "=" * 60)
        print(Fore.GREEN + f"   Binary Art Generator - Made with ❤️ by {self.creator_name}")
        print(Fore.CYAN + "=" * 60 + "\n")

    def step_1_request_image_path(self):
        print(Fore.YELLOW + "\n📸 STEP 1: Provide the Image")
        self.image_path = input("👉 Enter the full path to your image file: ").strip()
        if not os.path.isfile(self.image_path):
            print(Fore.RED + "❌ File not found. Please check the path and try again.")
            exit()

        # This code is shortened, intended to only display an example, not to show the entire code block 
```

### ABSTRACTION
Abstraction is the concept of hiding complex details while exposing only the necessary information to the user.
Simplifies the code and making it clean and neat for the user to understands.

```Python
    def step_5_save_all_outputs(self):
        print(Fore.YELLOW + "\n📂 STEP 5: Saving Files")

        text_path = os.path.join(self.output_directory, f"{self.base_filename}_binary_art.txt")
        with open(text_path, 'w') as file:
            file.write(self.binary_art)
        print(Fore.GREEN + f"✅ Saved as text: {text_path}")

        pdf_path = os.path.join(self.output_directory, f"{self.base_filename}_binary_art.pdf")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Courier", size=6)
        for line in self.binary_art.splitlines():
            pdf.cell(0, 4, txt=line, ln=1)
        pdf.output(pdf_path)
        print(Fore.GREEN + f"✅ Saved as PDF: {pdf_path}")

    def step_6_exit_message(self):
        print(Fore.CYAN + f"\n✨ Made with ❤️ by {self.creator_name}")
        print(Fore.CYAN + "👋 Program complete. Have a creative day!")

    def run(self):
        self.display_header()
        self.step_1_request_image_path()
        self.step_2_convert_image_to_binary()
        self.step_3_display_binary_art()

        if self.step_4_ask_to_save():
            self.step_5_save_all_outputs()
        else:
            print(Fore.YELLOW + "\n❎ Skipped saving files.")

        self.step_6_exit_message()
```

### Inheritance
Inheritance is the mechanism of basing an object or class upon another object or class, retaining a similar implementation. Also defined as deriving new classes from existing ones, such as a super class or base class, and then forming them into a hierarchy of classes.


### Polymorphism
Polymorphism, in object-oriented programming (OOP), is the ability of a variable, function, or object to take on multiple forms or behaviors. It allows you to treat objects of different classes uniformly through a common interface.





## Source Referrence 

This project was developed using knowledge and support of the following websites

For the Main Binary Image Converter:
[IMAGE TO ASCII CONVERTER](https://www.askpython.com/python/examples/turn-images-to-ascii-art-using-python)

For the Text and PDF Exportation Aspects of the Code:
[EXPORT to Text/PDF](https://www.geeksforgeeks.org/python/convert-text-and-text-file-to-pdf-using-python/)

For the Design and Colors of the Terminal itself:
[Text Design and Color](https://www.codu.co/articles/adding-colour-to-python-code-lbai_0u7)
