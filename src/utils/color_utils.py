"""
Color utility functions for the Milky Color Suite.

This module provides utility functions for color manipulation, generation,
and import/export operations.
"""

import random
from typing import Any
from typing import List
from typing import Union

from PIL import Image

from ..models.color_model import Color


def generate_harmonic_palette(
    base_color: Union[str, Color], harmony_type: str = "complementary", count: int = 8, include_base: bool = True
) -> List[Color]:
    """
    Generate a harmonious color palette based on color theory.

    Args:
        base_color: The base color to build the palette from
        harmony_type: The type of color harmony to use
            ("complementary", "analogous", "triadic", "tetradic", "monochromatic")
        count: The number of colors to generate
        include_base: Whether to include the base color in the palette

    Returns:
        A list of Color objects forming a harmonious palette
    """
    # Convert to Color object if string
    if isinstance(base_color, str):
        base_color = Color(base_color)

    palette = []

    # Add base color if requested
    if include_base:
        palette.append(base_color)

    # Generate colors based on harmony type
    if harmony_type == "analogous":
        # Add analogous colors
        angle = 30  # Default angle between analogous colors
        analogous = base_color.analogous(count=count, angle=angle)

        # Remove base color if it's included in analogous and we don't want to include it
        if not include_base:
            analogous = [c for c in analogous if c.hex != base_color.hex]

        palette.extend(analogous[: count - len(palette)])

    elif harmony_type == "complementary":
        # Add complementary color
        complement = base_color.complementary()
        palette.append(complement)

        # Fill remaining slots with variations
        remaining = count - len(palette)
        if remaining > 0:
            # Add variations of base and complement
            variations = []
            for i in range(remaining):
                if i % 2 == 0:
                    # Variation of base color
                    lightness = 0.1 + (i / remaining) * 0.6
                    variations.append(base_color.lighten(lightness))
                else:
                    # Variation of complementary color
                    lightness = 0.1 + ((i - 1) / remaining) * 0.6
                    variations.append(complement.lighten(lightness))

            palette.extend(variations[:remaining])

    elif harmony_type == "monochromatic":
        # Generate monochromatic variations
        h, s, lightness = base_color.hsl

        # Vary lightness for monochromatic scheme
        for i in range(count - len(palette)):
            # Distribute lightness values evenly
            new_lightness = 10 + (i * 80 / (count - 1))

            # Create new color with same hue/saturation but different lightness
            new_color = Color({"h": h, "s": s, "l": new_lightness})
            palette.append(new_color)

    elif harmony_type == "random":
        # Generate random colors
        for _ in range(count - len(palette)):
            h = random.randint(0, 360)
            s = random.randint(60, 100)
            lightness = random.randint(30, 70)
            palette.append(Color({"h": h, "s": s, "l": lightness}))

    elif harmony_type == "tetradic":
        # Add tetradic colors
        tetradic = base_color.tetradic()

        # Remove base color if it's included in tetradic and we don't want to include it
        if not include_base:
            tetradic = [c for c in tetradic if c.hex != base_color.hex]

        palette.extend(tetradic[: count - len(palette)])

        # Fill remaining slots with variations
        remaining = count - len(palette)
        if remaining > 0:
            # Add variations with different lightness
            variations = []
            for i in range(remaining):
                # Choose a color from the tetradic set
                source_color = tetradic[i % len(tetradic)]
                # Adjust lightness
                lightness = 0.1 + (i / remaining) * 0.6
                variations.append(source_color.lighten(lightness))

            palette.extend(variations[:remaining])

    elif harmony_type == "triadic":
        # Add triadic colors
        triadic = base_color.triadic()

        # Remove base color if it's included in triadic and we don't want to include it
        if not include_base:
            triadic = [c for c in triadic if c.hex != base_color.hex]

        palette.extend(triadic[: count - len(palette)])

        # Fill remaining slots with variations
        remaining = count - len(palette)
        if remaining > 0:
            # Add variations with different lightness
            variations = []
            for i in range(remaining):
                # Choose a color from the triadic set
                source_color = triadic[i % len(triadic)]
                # Adjust lightness
                lightness = 0.1 + (i / remaining) * 0.6
                variations.append(source_color.lighten(lightness))

            palette.extend(variations[:remaining])

        # If we're short, add variations of existing colors
    idx = 0
    # Ensure we have exactly the requested number of colors
    while len(palette) < count:
        source_color = palette[idx]

        # Alternate between lighter and darker variations
        if len(palette) % 2 == 0:
            new_color = source_color.lighten(0.1)
        else:
            new_color = source_color.darken(0.1)

        palette.append(new_color)

    # Trim if we have too many
    palette = palette[:count]

    return palette


def import_colors_from_image(image_path: str, count: int = 8, method: str = "dominant") -> List[Color]:
    """
    Extract colors from an image file.

    Args:
        image_path: Path to the image file
        count: Number of colors to extract
        method: Color extraction method: 'dominant', 'kmeans', or 'quantize'

    Returns:
        List of Color objects

    Raises:
        FileNotFoundError: If the image file is not found
        ValueError: If there is an error processing the image or the method is unsupported
        ImportError: If kmeans method is requested but scikit-learn is not installed
    """
    try:
        import numpy as np
    except ImportError as exc:
        raise ImportError("This function requires numpy. Please install it with: pip install numpy") from exc

    try:
        # Open the image
        img: Image.Image = Image.open(image_path)

        if method == "dominant":
            return _extracted_from_import_colors_from_image_37(img, np, count)
        elif method == "kmeans":
            try:
                # Optional dependency - imported at runtime
                # pip install scikit-learn
                from sklearn.cluster import KMeans
            except ImportError as exc:
                raise ImportError(
                    "K-means clustering requires scikit-learn. Please install it with: pip install scikit-learn"
                ) from exc

            # Resize for faster processing
            img_copy: Image.Image = img.copy()
            img_copy.thumbnail((100, 100))

            # Convert to RGB mode if necessary
            if img_copy.mode != "RGB":
                img_copy = img_copy.convert("RGB")

            # Get pixel data
            pixels = np.array(img_copy.getdata(), dtype=np.float64) / 255.0

            # Perform k-means clustering
            kmeans = KMeans(n_clusters=count)
            kmeans.fit(pixels)

            # Get the colors
            colors = kmeans.cluster_centers_

            # Convert to Color objects
            palette: List[Color] = []
            for color in colors:
                r, g, b = color
                palette.append(Color((r, g, b)))

            return palette

        elif method == "quantize":
            return _extracted_from_import_colors_from_image_114(img, count)
        else:
            raise ValueError(f"Unsupported extraction method: {method}")

    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Image file not found: {image_path}") from exc
    except Exception as e:
        raise ValueError(f"Error processing image: {e!s}") from e


def _extracted_from_import_colors_from_image_114(img: Image.Image, count: int) -> List[Color]:
    """
    Extract colors from an image using Pillow's quantization.

    Args:
        img: The image to extract colors from
        count: Number of colors to extract

    Returns:
        List of Color objects
    """
    # Use Pillow's quantization
    img_copy: Image.Image = img.copy()

    # Convert to RGB mode if necessary
    if img_copy.mode != "RGB":
        img_copy = img_copy.convert("RGB")

    # Quantize the image
    quantized = img_copy.quantize(colors=count)

    # Get the palette
    raw_palette = quantized.getpalette()
    if raw_palette is None:
        # Fallback if palette is None
        return _extracted_from_import_colors_from_image_37(img, __import__("numpy"), count)

    palette_data = raw_palette[: count * 3]

    # Convert to Color objects
    palette: List[Color] = []
    for i in range(0, len(palette_data), 3):
        r, g, b = palette_data[i : i + 3]
        color_hex = f"#{r:02x}{g:02x}{b:02x}"
        palette.append(Color(color_hex))

    return _extracted_from_import_colors_from_image_64(palette, count)


def _extracted_from_import_colors_from_image_37(img: Image.Image, np: Any, count: int) -> List[Color]:
    """
    Extract dominant colors from an image.

    Args:
        img: The image to extract colors from
        np: Numpy module (passed as argument to avoid global import)
        count: Number of colors to extract

    Returns:
        List of Color objects
    """
    # Simple method: resize and get dominant colors
    img_copy: Image.Image = img.copy()
    img_copy.thumbnail((100, 100))

    # Convert to RGB mode if necessary
    if img_copy.mode != "RGB":
        img_copy = img_copy.convert("RGB")

    # Get pixel data
    pixels = np.array(img_copy.getdata())

    # Find unique colors and their counts
    unique_colors, counts = np.unique(pixels, axis=0, return_counts=True)

    # Sort by count (most frequent first)
    indices = np.argsort(-counts)
    unique_colors = unique_colors[indices]

    # Convert to Color objects
    palette: List[Color] = []
    for i in range(min(count, len(unique_colors))):
        r, g, b = unique_colors[i]
        color_hex = f"#{r:02x}{g:02x}{b:02x}"
        palette.append(Color(color_hex))

    return _extracted_from_import_colors_from_image_64(palette, count)


def _extracted_from_import_colors_from_image_64(palette: List[Color], count: int) -> List[Color]:
    """
    Fill a palette to reach the requested color count.

    Args:
        palette: The existing palette to build upon
        count: Total number of colors required

    Returns:
        List of Color objects with the requested count
    """
    # Generate variants of existing colors
    idx = 0
    # Fill remaining slots if needed
    while len(palette) < count:
        source_color = palette[idx]

        # Alternate between lightening and darkening
        new_color = source_color.lighten(0.1) if len(palette) % 2 == 0 else source_color.darken(0.1)
        palette.append(new_color)

    return palette
