# ADD MultiLine Text to Image using Pillow

This script allows you to add multiline text to an image using the Pillow library and textwrap, providing a simple way to customize images with captions or descriptions.

## Features

- Add multiline text to images.
- Automatically adjusts the text wrapping to fit the image width.
- Supports custom font size and positioning.

## Prerequisites

- Python installed on your machine.
- Required Python packages: `Pillow`.

## Installation

1. Clone the repository or download the script.

    ```bash
    git clone https://github.com/your-username/MultiLine-text-to-image-using-pillow-and-textwrap.git
    cd MultiLine-text-to-image-using-pillow-and-textwrap
    ```

2. Install the required packages.

    ```bash
    pip install Pillow
    ```

## Usage

### For LANDSCAPE

1. Place your input image (`input.jpg`) in the same directory as the script.

2. Open a terminal and navigate to the script's directory.

3. Run the script with the following command:

    ```bash
    python multi_line_text.py
    ```

4. Check the output image (`changed.jpg`) in the same directory.

## Customization

- **Text:** You can customize the text by modifying the `text` variable in the script.
- **Font Size:** Adjust the `text_font` variable to change the font size.

## Troubleshooting

- If you encounter issues with the font, make sure the font file (`RussoOne-Regular.ttf`) is in the correct path.

## Example

```python
if __name__ == '__main__':
    input_image = 'input.jpg'
    text = 'Your custom multiline text goes here.'
    text_font = 25
    main(input_image, text, text_font)
```

![LandScape ](https://github.com/legerise/ytshortmaker/raw/master/assets/for-LANDSCAPE/changed.jpg)


### For PORTRAIT

Same as above just replace 'test.png' with your desired image also rename it to 'test.png' and run the script. If 
you don't want to rename it to 'test.png' you can edit the script to take image name instead of by-default 'test.png'

![Portrait ](https://github.com/legerise/ytshortmaker/raw/master/assets/for-PORTRAIT/test.png)

