# RaspberryPi_ESP32camstream
The provided code enables multiple ESP32-CAMs to stream live video to a Raspberry Pi for display and image classification.

# Follow these step-by-step instructions:

# Step 1: Upload Code to ESP32

Open the Arduino IDE (Integrated Development Environment) on your computer.
Make sure you have the ESP32 board package installed in the Arduino IDE. If not, go to "Tools" > "Board" > "Boards Manager," search for "ESP32," and install the package.
Connect your ESP32 board to your computer using a USB cable.
In the Arduino IDE, go to "Tools" > "Board" and select the appropriate ESP32 board from the list.
Go to "Tools" > "Port" and select the COM port to which your ESP32 is connected.
Copy the code you want to upload (the code for setting up the ESP32 as an Access Point and Wi-Fi client) into the Arduino IDE.
Click the "Upload" button (the right-arrow icon) to compile and upload the code to your ESP32 board. The code will be compiled, and the binary will be uploaded to the board.

# Step 2: Prepare Python Environment

Make sure you have Python installed on your computer. You can download Python from the official website (https://www.python.org/downloads/). For this code, Python 3 is recommended.
Install the necessary Python packages. Open a command prompt or terminal and run the following commands:

**pip install requests**
**pip install opencv-python**


# Step 3: Update Python Code

Copy the provided Python code (with the modifications for handling two ESP32-CAMs) into a Python file (e.g., RPI_src.py).
Replace '192.168.X.XX' and '192.168.X.XX' with the actual IP addresses of your two ESP32-CAMs.
Step 4: Run Python Code

Connect both ESP32-CAMs to your local Wi-Fi network. Make sure they are accessible with the specified IP addresses.
In the command prompt or terminal, navigate to the directory where you saved the RPI_src.py file.
Run the Python script using the following command:

**python RPI_src.py**

The Python script will start processing the video streams from both ESP32-CAMs and display them in separate windows using OpenCV.
