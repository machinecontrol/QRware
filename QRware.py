# Import required libraries
import qrcode  # Library for generating QR codes
from PIL import Image  # Library for image handling
import webbrowser  # Library for opening URLs in a web browser

# Function to generate a QR code from data and save it as an image
def generate_qr_code(data, filename="qr_code.png"):
    try:
        # Create a QRCode instance with specified settings
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        
        # Add the provided data to the QR code
        qr.add_data(data)
        qr.make(fit=True)  # Generate the QR code matrix to fit within the specified settings

        # Generate the QR code image with specified fill and background colors
        image = qr.make_image(fill_color="black", back_color="white")
        
        # Save the generated QR code image to a file
        image.save(filename)
        return filename  # Return the filename of the saved image
    except qrcode.exceptions.DataOverflowError:
        print("Error: Data provided is too large for a QR code.")
        return None
    except Exception as e:
        print("Error generating QR code:", e)
        return None  # Return None if an error occurs

# Function to open an image using the default image viewer
def open_image(filename):
    try:
        img = Image.open(filename)  # Open the specified image file
        img.show()  # Display the image using the default image viewer
    except FileNotFoundError:
        print("Error: QR code image not found.")
    except Exception as e:
        print("Error opening the image:", e)

# Function to open a website URL in a web browser
def open_website(url):
    try:
        webbrowser.open(url)  # Open the provided URL in a web browser
    except webbrowser.Error:
        print("Error: Failed to open the website.")
    except Exception as e:
        print("Error opening the website:", e)

# Main function
def main():
    try:
        # Prompt the user to input the website URL or payload
        website_url = input("Enter the website URL or payload: ")
        
        # Generate the QR code using the provided data
        image_filename = generate_qr_code(website_url)

        if image_filename:
            # If the QR code is successfully generated, display the filename
            print("QR code generated successfully:", image_filename)
            
            # Open the QR code image using the default image viewer
            open_image(image_filename)
            
            # Open the provided website URL in a web browser
            open_website(website_url)
    except KeyboardInterrupt:
        # Handle Ctrl+C interruption gracefully
        print("\nOperation aborted by user.")
    except Exception as e:
        # Handle any other exceptions that might occur
        print("An error occurred:", e)

# Entry point of the script
if __name__ == "__main__":
    main()  # Call the main function if the script is run directly
