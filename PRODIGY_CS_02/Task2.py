from PIL import Image
import numpy as np

def encrypt_image(image_path, key, operation='swap'):
    img = Image.open(image_path)
    pixels = np.array(img)
    
    if operation == 'swap':
        np.random.seed(key)
        np.random.shuffle(pixels)
    elif operation == 'add':
        pixels = (pixels + key) % 256
    
    encrypted_img = Image.fromarray(pixels)
    encrypted_img.save('encrypted_image.png')
    print('Image encrypted and saved as encrypted_image.png')

def decrypt_image(encrypted_image_path, key, operation='swap'):
    encrypted_img = Image.open(encrypted_image_path)
    pixels = np.array(encrypted_img)
    
    if operation == 'swap':
        np.random.seed(key)
        inverse_indices = np.argsort(np.random.permutation(pixels.size))
        pixels = pixels.flatten()[inverse_indices].reshape(pixels.shape)
    elif operation == 'add':
        pixels = (pixels - key) % 256
    
    decrypted_img = Image.fromarray(pixels)
    decrypted_img.save('decrypted_image.png')
    print('Image decrypted and saved as decrypted_image.png')

def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? (E/D): ").upper()
        if choice in ['E', 'D']:
            break
        else:
            print("Invalid choice. Please choose 'E' to encrypt or 'D' to decrypt.")
    
    image_path = input("Enter the path to the image: ")
    key = int(input("Enter the encryption/decryption key (integer): "))
    while True:
        operation = input("Choose operation: (swap) pixel values or (add) a constant value? (swap/add): ").lower()
        if operation in ['swap', 'add']:
            break
        else:
            print("Invalid operation. Please choose 'swap' or 'add'.")
    
    if choice == 'E':
        encrypt_image(image_path, key, operation)
    else:
        decrypt_image(image_path, key, operation)

if __name__ == "__main__":
    main()
