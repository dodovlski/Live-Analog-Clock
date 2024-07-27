# Analog Clock Application

This is a simple analog clock application created using Python's `turtle` module. The clock displays the current hour, minute, and second hands in a graphical interface.

## Requirements

- Python 3.x
- Turtle module (usually comes pre-installed with Python)

## How It Works

The application sets up a `turtle` graphics window and draws an analog clock face. It then updates the clock hands every second to reflect the current time.

### Main Components

1. **Screen Setup**
    - Sets up the screen with a size of 450x450 pixels.
    - Sets the background color to red.
    - Sets the window title to "Analog Clock Application".
    - Disables automatic screen updates for manual control.

2. **Turtle Setup**
    - Creates a turtle named `pen` to draw the clock.
    - Sets the drawing speed to the maximum.
    - Sets the pen size to 3.

3. **Draw Function**
    - Draws the clock face, hour markers, and the hands for hours, minutes, and seconds.

4. **Main Loop**
    - Continuously gets the current time.
    - Draws the clock hands based on the current time.
    - Updates the screen and clears the previous drawing to animate the clock hands.

## Running the Application

1. Save the code in a Python file, e.g., `analog_clock.py`.
2. Run the file using Python:
    ```sh
    python analog_clock.py
    ```
3. A window will appear displaying the analog clock, which updates every second.

## Customization

- **Screen Size and Background Color**: Change the screen setup parameters to adjust the size and color.
- **Clock Colors**: Adjust the colors used in the draw function for the clock face, hour markers, and hands.
- **Hand Lengths**: Modify the values for the lengths of the hour, minute, and second hands.

