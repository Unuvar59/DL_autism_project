import cv2
import os

def crop_faces_in_folder(input_folder, output_folder, face_cascade_path):
    # load the face cascade for face detection
    face_cascade = cv2.CascadeClassifier(face_cascade_path)

    # create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # clear the output folder if it already exists
    if os.path.exists(output_folder):
        for file in os.listdir(output_folder):
            file_path = os.path.join(output_folder, file)
            if os.path.isfile(file_path):
                os.remove(file_path)

    # iterate over all images in the folder
    for i, filename in enumerate(os.listdir(input_folder)):
        file_path = os.path.join(input_folder, filename)

        if not (filename.lower().endswith(".jpg") or filename.lower().endswith(".png") or filename.lower().endswith(".jpeg")):
            continue

        # load the image
        image = cv2.imread(file_path)
        if image is None:
            print(f"Image couldn't upload: {file_path}")
            continue

        # convert the image to grayscale for face detection
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # detect faces in the image
        faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(faces) == 0:
            print(f"Face couldn't load: {file_path}")
            continue

        # get the first face found 
        x, y, w, h = faces[0]  # get the first face found

        # crop the image 
        cropped_image = image[y:y+h, x:x+w]

        # save the cropped image
        output_filename = f"ours_{i+1}.jpg"
        output_path = os.path.join(output_folder, output_filename)
        cv2.imwrite(output_path, cropped_image)
        print(f"Cropped image is saved: {output_path}")

# main function
if __name__ == "__main__":

    haarcascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

    # Input and output folders
    input_folder = "images_to_prep"  
    output_folder = "cropped_images"  

    # run the function
    crop_faces_in_folder(input_folder, output_folder, haarcascade_path)