"""
Color utility functions for the Milky Color Suite.

This module provides utility functions for color manipulation, generation,
and import/export operations.
"""

import math
import random
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

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
        h, s, l = base_color.hsl

        # Vary lightness for monochromatic scheme
        for i in range(count - len(palette)):
            # Distribute lightness values evenly
            new_l = 10 + (i * 80 / (count - 1))

            # Create new color with same hue/saturation but different lightness
            new_color = Color({"h": h, "s": s, "l": new_l})
            palette.append(new_color)

    elif harmony_type == "random":
        # Generate random colors
        for _ in range(count - len(palette)):
            h = random.randint(0, 360)
            s = random.randint(60, 100)
            l = random.randint(30, 70)
            palette.append(Color({"h": h, "s": s, "l": l}))

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
    Extract a color palette from an image.

    Args:
        image_path: Path to the image file
        count: Number of colors to extract
        method: Method to use for extraction ("dominant", "kmeans", "quantize")

    Returns:
        A list of Color objects extracted from the image

    Raises:
        ImportError: If required libraries are not installed
        FileNotFoundError: If the image file does not exist
        ValueError: If the image cannot be processed
    """
    try:
        import numpy as np
        from PIL import Image
    except ImportError as e:
        raise ImportError(
            "Image processing requires additional libraries. Please install them with: pip install pillow numpy"
        ) from e

    try:
        # Open the image
        img = Image.open(image_path)

        if method == "dominant":
            return _extracted_from_import_colors_from_image_37(img, np, count)
        elif method == "kmeans":
            try:
                from sklearn.cluster import KMeans
            except ImportError as exc:
                raise ImportError(
                    "K-means clustering requires scikit-learn. Please install it with: pip install scikit-learn"
                ) from exc

            # Resize for faster processing
            img = img.copy()
            img.thumbnail((100, 100))

            # Convert to RGB mode if necessary
            if img.mode != "RGB":
                img = img.convert("RGB")

            # Get pixel data
            pixels = np.array(img.getdata(), dtype=np.float64) / 255.0

            # Perform k-means clustering
            kmeans = KMeans(n_clusters=count)
            kmeans.fit(pixels)

            # Get the colors
            colors = kmeans.cluster_centers_

            # Convert to Color objects
            palette = []
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


# TODO Rename this here and in `import_colors_from_image`
def _extracted_from_import_colors_from_image_114(img, count):
    # Use Pillow's quantization
    img = img.copy()

    # Convert to RGB mode if necessary
    if img.mode != "RGB":
        img = img.convert("RGB")

    # Quantize the image
    quantized = img.quantize(colors=count)

    # Get the palette
    palette_data = quantized.getpalette()[: count * 3]

    # Convert to Color objects
    palette = []
    for i in range(0, len(palette_data), 3):
        r, g, b = palette_data[i : i + 3]
        color_hex = f"#{r:02x}{g:02x}{b:02x}"
        palette.append(Color(color_hex))

    return _extracted_from_import_colors_from_image_64(palette, count)


# TODO Rename this here and in `import_colors_from_image`
def _extracted_from_import_colors_from_image_37(img, np, count):
    # Simple method: resize and get dominant colors
    img = img.copy()
    img.thumbnail((100, 100))

    # Convert to RGB mode if necessary
    if img.mode != "RGB":
        img = img.convert("RGB")

    # Get pixel data
    pixels = np.array(img.getdata())

    # Find unique colors and their counts
    unique_colors, counts = np.unique(pixels, axis=0, return_counts=True)

    # Sort by count (most frequent first)
    indices = np.argsort(-counts)
    unique_colors = unique_colors[indices]

    # Convert to Color objects
    palette = []
    for i in range(min(count, len(unique_colors))):
        r, g, b = unique_colors[i]
        color_hex = f"#{r:02x}{g:02x}{b:02x}"
        palette.append(Color(color_hex))

    return _extracted_from_import_colors_from_image_64(palette, count)


# TODO Rename this here and in `import_colors_from_image`
def _extracted_from_import_colors_from_image_64(palette, count):
    # Generate variants of existing colors
    idx = 0
    # Fill remaining slots if needed
    while len(palette) < count:
        source_color = palette[idx]

        # Alternate between lightening and darkening
        new_color = source_color.lighten(0.1) if len(palette) % 2 == 0 else source_color.darken(0.1)
        palette.append(new_color)

    return palette
