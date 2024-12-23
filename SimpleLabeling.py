import os
import csv
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk

class ImageLabelingApp:
    def __init__(self, master, image_folder, csv_file='image_labels.csv'):
        self.master = master
        self.image_folder = image_folder
        self.csv_file = csv_file
        self.image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
        self.existing_labels = self.load_existing_labels()
        self.image_files = [img for img in self.image_files if img not in self.existing_labels]  # Exclude images that are already labeled
        self.current_index = 0
        
        if not self.image_files:
            self.show_message("All images are labeled!")
            return

        self.current_image_path = None

        # UI elements
        self.label = Label(master)
        self.label.pack()

        self.buttons_frame = tk.Frame(master)
        self.buttons_frame.pack()

        self.happy_button = Button(self.buttons_frame, text="😊 Happy", command=lambda: self.save_label(0))
        self.happy_button.pack(side="left")

        self.sad_button = Button(self.buttons_frame, text="🙢 Sad", command=lambda: self.save_label(1))
        self.sad_button.pack(side="left")

        self.angry_button = Button(self.buttons_frame, text="😠 Angry", command=lambda: self.save_label(2))
        self.angry_button.pack(side="left")

        self.surprised_button = Button(self.buttons_frame, text="😮 Surprised", command=lambda: self.save_label(3))
        self.surprised_button.pack(side="left")

        self.neutral_button = Button(self.buttons_frame, text="😐 Neutral", command=lambda: self.save_label(4))
        self.neutral_button.pack(side="left")

        self.remove_button = Button(self.buttons_frame, text="🗑️ Remove", command=self.remove_image)
        self.remove_button.pack(side="left")

        self.quit_button = Button(self.buttons_frame, text="🚪 Quit", command=self.quit_app)
        self.quit_button.pack(side="left")

        self.load_image()
    
    def load_existing_labels(self):
        """Reads previously labeled images from the CSV file and adds them to a dictionary."""
        if os.path.exists(self.csv_file):
            with open(self.csv_file, 'r') as file:
                reader = csv.reader(file)
                return {rows[0]: rows[1] for rows in reader}  # {'image1.jpg': '0', ...}
        return {}

    def load_image(self):
        """Loads the next image."""
        if self.current_index < len(self.image_files):
            image_path = os.path.join(self.image_folder, self.image_files[self.current_index])
            self.current_image_path = image_path
            img = Image.open(image_path).resize((400, 400))  # Resize the image
            img_tk = ImageTk.PhotoImage(img)
            self.label.config(image=img_tk)
            self.label.image = img_tk  # Without this line, the image will not be displayed
            self.show_message(f"Image: {os.path.basename(image_path)} ({self.current_index+1}/{len(self.image_files)})")
        else:
            self.show_message("All images are labeled!")
            self.master.quit()

    def save_label(self, label):
        """Saves the label and moves to the next image."""
        if self.current_image_path:
            with open(self.csv_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([os.path.basename(self.current_image_path), label])  # Write image name and label to CSV
            print(f"{os.path.basename(self.current_image_path)} saved with label ({label}).")
        
        self.current_index += 1
        self.load_image()
    
    def remove_image(self):
        """Removes the current image from the dataset and CSV file."""
        if self.current_image_path:
            # Delete image file
            os.remove(self.current_image_path)
            print(f"{os.path.basename(self.current_image_path)} removed from dataset.")
            
            # Remove from CSV if it exists
            if os.path.exists(self.csv_file):
                with open(self.csv_file, 'r') as file:
                    rows = [row for row in csv.reader(file) if row[0] != os.path.basename(self.current_image_path)]
                with open(self.csv_file, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
                print(f"{os.path.basename(self.current_image_path)} removed from CSV.")
            
            # Remove from image list and load the next image
            self.image_files.pop(self.current_index)
        
        self.load_image()

    def show_message(self, message):
        """Displays a message."""
        self.label.config(text=message)
    
    def quit_app(self):
        """Closes the application."""
        print("Exiting the application...")
        self.master.quit()


# # # Start the program for ASD
# if __name__ == "__main__":
#     root = tk.Tk()
#     image_folder = "FADC-Dataset/ASD/"  # Folder containing images
#     app = ImageLabelingApp(root, image_folder, csv_file='image_labels_asd.csv')
#     root.mainloop()

# Start the program for TD
if __name__ == "__main__":
    root = tk.Tk()
    image_folder = "FADC-Dataset/TD/"  # Folder containing images
    app = ImageLabelingApp(root, image_folder, csv_file='image_labels_td.csv')
    root.mainloop()
