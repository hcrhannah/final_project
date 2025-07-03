import os
from PIL import Image
from fpdf import FPDF
from colorama import Fore, Style, init

init(autoreset=True)

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

    def step_2_convert_image_to_binary(self):
        print(Fore.YELLOW + "\n🛠️  STEP 2: Processing the Image into Binary Art")
        try:
            image = Image.open(self.image_path).convert('L')
        except Exception as error:
            print(Fore.RED + f"❌ Error loading image: {error}")
            exit()

        width, height = image.size
        aspect_ratio = height / width
        new_width = 200
        new_height = int(aspect_ratio * new_width * 0.5)
        image = image.resize((new_width, new_height))

        pixels = image.getdata()
        self.binary_art = ""
        for row in range(new_height):
            for col in range(new_width):
                pixel_index = row * new_width + col
                pixel_value = pixels[pixel_index]
                self.binary_art += '1' if pixel_value > 128 else '0'
            self.binary_art += '\n'

        self.output_directory = os.path.dirname(self.image_path)
        self.base_filename = os.path.splitext(os.path.basename(self.image_path))[0]

    def step_3_display_binary_art(self):
        print(Fore.YELLOW + "\n🎨 STEP 3: Generated Binary Art\n")
        print(Style.BRIGHT + Fore.WHITE + self.binary_art)

    def step_4_ask_to_save(self) -> bool:
        print(Fore.YELLOW + "\n💾 STEP 4: Save the Binary Art?")
        user_input = input(Fore.GREEN + "👉 Type 'yes' to save as .txt and .pdf, or anything else to exit: ").strip().lower()
        return user_input == 'yes'

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


if __name__ == "__main__":
    generator = BinaryArtGenerator(creator_name="Hannah Sophia Hacar")
    generator.run()
    
