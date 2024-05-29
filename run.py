import os
import cv2

list_of_names = []


def delete_old_data():
    for i in os.listdir("generated-certificates/"):
        os.remove("generated-certificates/{}".format(i))


def cleanup_data():
    with open('name-data.txt') as f:
        for line in f:
            list_of_names.append(line.strip())


def generate_certificates():
    for index, name in enumerate(list_of_names):
        certificate_template_image = cv2.imread("final-template.png")
        # Use the Archive font with italics
        font = cv2.FONT_HERSHEY_TRIPLEX | cv2.FONT_ITALIC
        # Set the font size and color (blue in BGR format)
        font_size = 3
        font_color = (173, 82, 54)  # Blue in BGR format
        # Put the text on the image
        cv2.putText(
            certificate_template_image,
            name.strip(),
            (114, 630),
            font,
            font_size,
            font_color,
            8,
            cv2.LINE_AA,
        )
        # Save the certificate
        cv2.imwrite("generated-certificates/{}.jpg".format(name.strip()), certificate_template_image)
        print("Processing {} / {}".format(index + 1, len(list_of_names)))


def main():
    delete_old_data()
    cleanup_data()
    generate_certificates()


if __name__ == '__main__':
    main()
