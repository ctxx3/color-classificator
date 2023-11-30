# Color Classificator

## Overview

This Python project focuses on color classification, providing a robust solution for categorizing colors and returning their CC Tweaked closest equivalents.

## Features

- **Color Extraction**: Easily extract color information from images.
- **Classification Models**: Utilizes simple machine learning models for faster and accurate color categorization.
- **User-Friendly**: Simple and intuitive functions for seamless integration.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/ctxx3/color-classificator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd color-classificator
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Import the `ColorClassifier` class into your Python script:

   ```python
   from color_classificator import ColorClassifier, color_list
   ```

2. Create an instance of the `ColorClassifier` class:

   ```python
   classifier = ColorClassifier()
   ```

3. Use the `classify_color` method to categorize a color:

   ```python
   color_id = classifier.classify_color((0,255,0)  # Replace with your color

   new_color = color_list[color_id]
   
   print(f"CC Tweaked equivalent:  {new_color}.")
   ```

## Examples

Check out the `examples` directory for usage examples and integration guides.

## Contributing

Contributions are welcome! If you have ideas for improvement or encounter any issues, please submit a pull request or open an issue.

## License

This project is licensed under the MPL License - see the [LICENSE](LICENSE) file for details.
