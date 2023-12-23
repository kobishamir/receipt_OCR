# receipt_OCR

```markdown
This repository contains a Python script for processing receipt images, recognizing text using OCR, and exporting the data to a Google Sheets document.

- **Image Processing**: The script can perform basic image processing tasks such as resizing, binary thresholding, and inverting images using OpenCV.
- **Command Line Interface**: The script uses argparse to allow users to specify the image file and binary threshold value from the command line.

## Future Features

- **OCR**: The script will be able to recognize text in receipt images using an OCR engine.
- **Data Extraction**: The script will extract relevant data from the recognized text.
- **Google Sheets Export**: The script will export the extracted data to a specified Google Sheets document. If the document name and other necessary information are provided, the script will add the new data as a new line in the document.

## Usage

The script can be run from the command line with the following syntax:

```bash
python main.py -i <image_path> -t <threshold>
```

Here, `<image_path>` should be replaced with the path to the receipt image file you want to process, and `<threshold>` should be replaced with the threshold value you want to use for binary thresholding.

## Requirements

- Python 3.6 or later
- OpenCV
- argparse

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

[MIT](https://choosealicense.com/licenses/mit/)
```

This README provides a brief overview of your script, explains its current features, and outlines the features you plan to add in the future. It also provides usage instructions and mentions the requirements for running the script.

You can customize this template to better fit your project. For example, you might want to add more detailed explanations of your script's features, include examples of the script's output, or provide information about how to install the required packages.

Let me know if you need further assistance!
