# Color Model API Documentation

This document provides detailed information about the `Color` class in the Palette Milker application. The `Color` model enables color creation, conversion between different color formats, manipulation, and analysis.

## Class Overview

```python
class Color:
    """Color model for representing and manipulating colors."""
```

The `Color` class provides a comprehensive set of functionalities for working with colors in various formats (HEX, RGB, HSL) and performing operations like comparing, lightening, darkening, and generating color harmonies.

## Initialization

### Constructor

```python
def __init__(self, value: str) -> None:
    """
    Initialize a color from a hex color string.
    
    Args:
        value: Hex color string (with or without leading #)
        
    Raises:
        ValueError: If the hex color string is invalid
    """
```

Example usage:
```python
# Create a color from a hex string with a hash symbol
red_color = Color("#FF0000")

# Create a color from a hex string without a hash symbol
blue_color = Color("0000FF")
```

### Static Factory Methods

#### from_rgb

```python
@staticmethod
def from_rgb(red: int, green: int, blue: int) -> 'Color':
    """
    Create a color from RGB values.
    
    Args:
        red: Red component (0-255)
        green: Green component (0-255)
        blue: Blue component (0-255)
        
    Returns:
        A new Color instance
        
    Raises:
        ValueError: If any component is outside the valid range
    """
```

Example usage:
```python
# Create a color from RGB values
yellow = Color.from_rgb(255, 255, 0)
```

#### from_hsl

```python
@staticmethod
def from_hsl(hue: float, saturation: float, lightness: float) -> 'Color':
    """
    Create a color from HSL values.
    
    Args:
        hue: Hue angle in degrees (0-360)
        saturation: Saturation percentage (0-100)
        lightness: Lightness percentage (0-100)
        
    Returns:
        A new Color instance
        
    Raises:
        ValueError: If any component is outside the valid range
    """
```

Example usage:
```python
# Create a color from HSL values
purple = Color.from_hsl(270, 100, 50)
```

## Properties

### Basic Properties

| Property | Type | Description |
|----------|------|-------------|
| `hex` | `str` | Hex representation of the color (e.g., "#FF0000") |
| `rgb` | `Tuple[int, int, int]` | RGB components as a tuple (e.g., (255, 0, 0)) |
| `hsl` | `Tuple[float, float, float]` | HSL components as a tuple (e.g., (0, 100, 50)) |
| `red` | `int` | Red component (0-255) |
| `green` | `int` | Green component (0-255) |
| `blue` | `int` | Blue component (0-255) |
| `hue` | `float` | Hue angle in degrees (0-360) |
| `saturation` | `float` | Saturation percentage (0-100) |
| `lightness` | `float` | Lightness percentage (0-100) |
| `luminance` | `float` | Perceived luminance (0-1) of the color |

## Methods

### Color Comparison

#### contrast_ratio

```python
def contrast_ratio(self, other: 'Color') -> float:
    """
    Calculate the contrast ratio between this color and another color.
    
    Args:
        other: Another color to compare with
        
    Returns:
        Contrast ratio between 1:1 and 21:1
    """
```

Example usage:
```python
white = Color("#FFFFFF")
black = Color("#000000")
ratio = white.contrast_ratio(black)  # Returns approximately 21.0
```

#### is_dark

```python
def is_dark(self, threshold: float = 0.5) -> bool:
    """
    Determine if the color is considered dark.
    
    Args:
        threshold: Luminance threshold (0-1) for considering a color dark
        
    Returns:
        True if the color is dark, False otherwise
    """
```

#### is_light

```python
def is_light(self, threshold: float = 0.5) -> bool:
    """
    Determine if the color is considered light.
    
    Args:
        threshold: Luminance threshold (0-1) for considering a color light
        
    Returns:
        True if the color is light, False otherwise
    """
```

### Color Manipulation

#### lighten

```python
def lighten(self, amount: float) -> 'Color':
    """
    Create a lighter version of this color.
    
    Args:
        amount: Amount to lighten (0-100)
        
    Returns:
        A new Color instance
    """
```

Example usage:
```python
gray = Color("#808080")
lighter_gray = gray.lighten(20)  # Makes the color 20% lighter
```

#### darken

```python
def darken(self, amount: float) -> 'Color':
    """
    Create a darker version of this color.
    
    Args:
        amount: Amount to darken (0-100)
        
    Returns:
        A new Color instance
    """
```

Example usage:
```python
orange = Color("#FF8800")
darker_orange = orange.darken(25)  # Makes the color 25% darker
```

### Color Harmonies

#### get_complementary

```python
def get_complementary(self) -> 'Color':
    """
    Get the complementary color (opposite on the color wheel).
    
    Returns:
        A new Color instance
    """
```

Example usage:
```python
red = Color("#FF0000")
cyan = red.get_complementary()  # Returns #00FFFF
```

#### get_analogous

```python
def get_analogous(self, angle: float = 30, count: int = 2) -> List['Color']:
    """
    Get analogous colors (adjacent on the color wheel).
    
    Args:
        angle: Angle between colors (degrees)
        count: Number of analogous colors to generate
        
    Returns:
        List of Color instances
    """
```

Example usage:
```python
blue = Color("#0000FF")
analogous_colors = blue.get_analogous()  # Returns colors 30° to each side
```

#### get_triadic

```python
def get_triadic(self) -> List['Color']:
    """
    Get triadic colors (three colors evenly spaced on the color wheel).
    
    Returns:
        List of two Color instances (with the current color, forms a triad)
    """
```

#### get_tetradic

```python
def get_tetradic(self) -> List['Color']:
    """
    Get tetradic colors (four colors evenly spaced on the color wheel).
    
    Returns:
        List of three Color instances (with the current color, forms a tetrad)
    """
```

#### get_split_complementary

```python
def get_split_complementary(self, angle: float = 30) -> List['Color']:
    """
    Get split-complementary colors.
    
    Args:
        angle: Angle of split from complementary (degrees)
        
    Returns:
        List of two Color instances
    """
```

## Utility Methods

### String Representation

```python
def __str__(self) -> str:
    """Return the hex representation of the color."""
    return self.hex

def __repr__(self) -> str:
    """Return a string representation for developers."""
    return f"Color('{self.hex}')"
```

### Equality Comparison

```python
def __eq__(self, other: Any) -> bool:
    """
    Compare two colors for equality.
    
    Args:
        other: Another object to compare with
        
    Returns:
        True if both objects are colors with the same RGB values
    """
```

## Example Usage

```python
# Create colors
red = Color("#FF0000")
blue = Color("#0000FF")
yellow = Color.from_rgb(255, 255, 0)
purple = Color.from_hsl(270, 100, 50)

# Access properties
print(f"Red in hex: {red.hex}")
print(f"Red in RGB: {red.rgb}")
print(f"Red in HSL: {red.hsl}")

# Check if colors are dark or light
print(f"Is blue dark? {blue.is_dark()}")  # True
print(f"Is yellow light? {yellow.is_light()}")  # True

# Calculate contrast ratio
contrast = yellow.contrast_ratio(purple)
print(f"Contrast ratio between yellow and purple: {contrast:.1f}:1")

# Generate color variations
light_red = red.lighten(20)
dark_red = red.darken(20)

# Generate color harmonies
complementary = red.get_complementary()
analogous = red.get_analogous()
triadic = red.get_triadic()
```

## Color Conversion Methods

These are internal methods used by the Color class for converting between different color formats:

### rgb_to_hsl

```python
@staticmethod
def _rgb_to_hsl(r: int, g: int, b: int) -> Tuple[float, float, float]:
    """
    Convert RGB to HSL.
    
    Args:
        r: Red component (0-255)
        g: Green component (0-255)
        b: Blue component (0-255)
        
    Returns:
        HSL values as (hue, saturation, lightness)
    """
```

### hsl_to_rgb

```python
@staticmethod
def _hsl_to_rgb(h: float, s: float, l: float) -> Tuple[int, int, int]:
    """
    Convert HSL to RGB.
    
    Args:
        h: Hue angle in degrees (0-360)
        s: Saturation percentage (0-100)
        l: Lightness percentage (0-100)
        
    Returns:
        RGB values as (red, green, blue)
    """
```
