# Mosffel

[Japanese Ver.](https://github.com/takty/mosffel/blob/main/README.ja.md)

## Introduction

**Mosffel** is a monospaced font based on the block style commonly taught in Japanese elementary and middle schools. It is designed to connect English learning with programming, allowing children who have learned to write in this style to comfortably engage with coding. This font is unique in being both block-style and monospaced, making it suitable for programming and text editing.

## Installation

**Mosffel** is distributed in ZIP format. Please follow the steps below to install the OpenType font.

### Windows

1. Extract the ZIP file.
1. Right-click on the font file (`.otf`) and select "Install."

### macOS

1. Extract the ZIP file.
1. Double-click the font file (`.otf`) to open the Font Book.
1. Click "Install Font."

### Linux

1. Extract the ZIP file.
1. Copy the font file (`.otf`) to the `.fonts` directory in your home folder.
1. Run `fc-cache -fv` in the terminal to update the font cache.

### Using as a Web Font

To use it as a web font, convert the `.otf` file to `.woff` or `.woff2` format and specify it in your CSS.

## Usage

**Mosffel** currently includes characters only within the ASCII range, primarily supporting the alphanumeric and symbol characters used in programming languages. Therefore, it is recommended to use this font in combination with other fonts.

### Example Usage in CSS

Below is a sample CSS code for using Mosffel in combination with other fonts as a web font.

```css
body {
    font-family: 'Mosffel', 'Courier New', monospace;
}
```

In this example, Mosffel is applied to the specified character range, while other characters are rendered using Courier New or the system's default monospace font.

## License

**Mosffel** is licensed under the [SIL Open Font License 1.1](https://scripts.sil.org/OFL). This license allows you to freely use, modify, and redistribute the font. Commercial use is also permitted.

If you redistribute a modified version of this font, please use a different name than the original font.

If you use this font or come across it in use, I'd be delighted if you could let me know in some way.

## Copyright and Credits

The copyright for the **Mosffel** font belongs to **Takuto Yanagida**.

## Changelog

- **Version 1.0** - Initial release (Sep. 2, 2024)
