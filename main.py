import os
from PIL import Image
from PIL import ImageFilter
import matplotlib.pyplot as plt


def load_image(image_path):
    """Завантажує зображення з локальної директорії."""
    try:
        if os.path.exists(image_path):
            img = Image.open(image_path)
            return img
        else:
            raise FileNotFoundError(f"Image not found at path: {image_path}")
    except Exception as e:
        print(f"Error loading image: {e}")
        return None


def zoom_in(img, scale_factor):
    """Приближення зображення шляхом зміни його масштабу."""
    width, height = img.size
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)

    # Зміна розміру зображення
    img_zoomed = img.resize((new_width, new_height), Image.LANCZOS)

    return img_zoomed


def process_image(img):
    """Обробка зображення для виявлення контурів."""
    if img is None:
        print("No image to process.")
        return None

    image_filter = img.filter(ImageFilter.FIND_EDGES)

    # Перетворення в чорно-біле
    #img_gray = img.convert('L')

    # Розмиття зображення
    #img_blurred = img_gray.filter(ImageFilter.GaussianBlur(radius=2))

    # Порогова обробка
    #threshold = 128
    #mg_thresholded = image_filter.point(lambda p: p > threshold and 255)

    # Виявлення контурів
    #img_edges = img_thresholded.filter(ImageFilter.FIND_EDGES)
    img_edges = zoom_in(image_filter, 1.5)
    return img_edges


def display_image(img):
    """Виводить зображення через matplotlib."""
    if img is not None:
        plt.imshow(img, cmap='gray')
        plt.axis('off')
        plt.show()


def main():
    # Вкажіть шлях до зображення в локальній директорії
    image_path = "images/test_piramyd.jfif"  # Змініть на ваш шлях до зображення

    # Завантаження зображення
    img = load_image(image_path)

    if img is not None:
        processed_img = process_image(img)
        display_image(processed_img)
    else:
        print("Failed to download or load the image.")


if __name__ == "__main__":
    main()

