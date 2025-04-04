# UTTER Array Format - Python Implementation

This document covers the conversion of the UTTER (Unified Tiled Tone Export Resource) array format from CoffeeScript to Python for use with the Textual framework implementation of Milky Color Suite.

## Overview

The UTTER format is a dynamic template system for exporting color palettes in a structured way, primarily designed for CSS variable generation but flexible enough for other export formats. It organizes colors into "bottles" - logical groupings of related color variables.

## Python Implementation

```python
# milky_suite/utils/utter.py

class UTTER:
    """
    UTTER Array Format - Dynamic Template for Color Palette Export
    
    This class defines a template system for organizing and exporting colors
    in a structured format. Colors are organized into "bottles" - logical 
    groupings like backgrounds, themes, borders, etc.
    """
    
    @classmethod
    def create_from_palette(cls, palette):
        """
        Factory method to create a new UTTER instance with palette colors.
        
        Args:
            palette (dict): A dictionary of color values keyed by name
                           (e.g. {'primary': '#FF5500', 'secondary': '#333333'})
        
        Returns:
            UTTER: A new instance with all bottle templates populated with actual colors
        """
        instance = cls()
        instance.bottles = {}
        
        # Populate bottle templates with actual colors from palette
        for bottle_name, bottle_template in cls.BOTTLE_TEMPLATES.items():
            instance.bottles[bottle_name] = {}
            for var_name, color_ref in bottle_template.items():
                # If the value is a special format string (e.g., spacing, sizing)
                if isinstance(color_ref, str) and not color_ref.startswith('$'):
                    instance.bottles[bottle_name][var_name] = color_ref
                # If the value is a color reference
                else:
                    color_key = color_ref[1:] if color_ref.startswith('$') else color_ref
                    instance.bottles[bottle_name][var_name] = palette.get(color_key, '#000000')
        
        return instance
    
    def to_css(self):
        """
        Convert UTTER bottles to CSS variables.
        
        Returns:
            str: CSS variable definitions as a string
        """
        css = []
        for bottle_name, bottle in self.bottles.items():
            css.append(f"/* Bottles - {bottle_name} */")
            for var_name, value in bottle.items():
                css.append(f"--{var_name}: {value};")
            css.append("")  # Empty line between bottles
        
        return "\n".join(css)
    
    def get_bottle(self, name):
        """
        Get a specific bottle by name.
        
        Args:
            name (str): The name of the bottle to retrieve
            
        Returns:
            dict: The bottle variables or None if not found
        """
        return self.bottles.get(name, {})
    
    def merge_bottles(self, *bottle_names):
        """
        Merge multiple bottles into a single dictionary.
        
        Args:
            *bottle_names: Variable number of bottle names to merge
            
        Returns:
            dict: Merged variables from all specified bottles
        """
        result = {}
        for name in bottle_names:
            bottle = self.get_bottle(name)
            result.update(bottle)
        return result
    
    def create_custom_bottle(self, name, variables):
        """
        Create a new custom bottle.
        
        Args:
            name (str): Name for the new bottle
            variables (dict): Variables to include in the bottle
            
        Returns:
            self: For method chaining
        """
        self.bottles[name] = variables
        return self
    
    def to_dict(self):
        """
        Convert the entire UTTER structure to a dictionary.
        
        Returns:
            dict: Dictionary representation of all bottles
        """
        return self.bottles
    
    def to_json(self):
        """
        Convert the entire UTTER structure to JSON.
        
        Returns:
            str: JSON representation of all bottles
        """
        import json
        return json.dumps(self.bottles, indent=2)

    # Bottle templates - define the structure and color references
    # $ prefix indicates a dynamic color value to be filled from palette
    BOTTLE_TEMPLATES = {
        # Background variables for different UI elements
        "Backgrounds": {
            "background-primary": "$primary",
            "background-secondary": "$secondary",
            "background-tertiary": "$tertiary",
            "background-dark": "$dark",
            "background-light": "$light",
            "background-alt": "$altBackground",
            "background-overlay": "$overlay",
            "background-hover": "$hoverBackground",
            "background-active": "$activeBackground",
            "background-disabled": "$disabledBackground",
            "background-card": "$cardBackground",
            "background-modal": "$modalBackground",
            "background-dropdown": "$dropdownBackground",
            "background-tooltip": "$tooltipBackground",
            "background-inset": "$insetBackground",
            "background-elevated": "$elevatedBackground",
            "background-sunken": "$sunkenBackground",
        },
        
        # Themed variables for consistent look and feel
        "Themes": {
            "text-primary": "$textPrimary",
            "text-secondary": "$textSecondary",
            "text-tertiary": "$textTertiary",
            "text-muted": "$textMuted",
            "text-disabled": "$textDisabled",
            "text-inverse": "$textInverse",
            "text-link": "$linkColor",
            "text-link-hover": "$linkHoverColor",
            "text-error": "$errorText",
            "text-success": "$successText",
            "text-warning": "$warningText",
            "text-info": "$infoText",
            "primary": "$primary",
            "secondary": "$secondary",
            "tertiary": "$tertiary",
            "accent-color": "$accent",
            "accent-color-hover": "$accentHover",
            "secondary-accent-color": "$secondaryAccent",
            "secondary-accent-color-hover": "$secondaryAccentHover",
            "tertiary-accent-color": "$tertiaryAccent",
            "tertiary-accent-color-hover": "$tertiaryAccentHover",
        },
        
        # Border styling variables
        "Borders": {
            "border-color": "$borderColor",
            "border-color-light": "$borderColorLight",
            "border-color-dark": "$borderColorDark",
            "border-color-accent": "$borderColorAccent",
            "border-color-focus": "$borderColorFocus",
            "border-color-error": "$borderColorError",
            "border-color-success": "$borderColorSuccess",
            "border-color-warning": "$borderColorWarning",
            "border-radius-small": "2px",  # Non-color values remain unchanged
            "border-radius-medium": "4px",
            "border-radius-large": "8px",
            "border-radius-xlarge": "12px",
            "border-radius-rounded": "9999px",
            "border-width-thin": "1px",
            "border-width-medium": "2px",
            "border-width-thick": "3px",
            "border-style-solid": "solid",
            "border-style-dashed": "dashed",
            "border-style-dotted": "dotted",
        },
        
        # Shadow effects for depth and elevation
        "Shadows": {
            "shadow-small": "0 1px 3px $shadowColorA, 0 1px 2px $shadowColorB",
            "shadow-medium": "0 3px 6px $shadowColorA, 0 2px 4px $shadowColorB",
            "shadow-large": "0 10px 20px $shadowColorA, 0 3px 6px $shadowColorB",
            "shadow-xlarge": "0 14px 28px $shadowColorA, 0 10px 10px $shadowColorB",
            "shadow-inner": "inset 0 2px 4px $shadowColorInner",
            "shadow-outline": "0 0 0 3px $focusRingColor",
            "shadow-focus": "0 0 0 3px $focusRingColorSecondary",
            "shadow-none": "none",
        },
        
        # Form element styling variables
        "Forms": {
            "input-background": "$inputBackground",
            "input-border": "$inputBorder",
            "input-color": "$inputText",
            "input-placeholder": "$inputPlaceholder",
            "input-disabled-background": "$inputDisabledBg",
            "input-disabled-color": "$inputDisabledText",
            "input-focus-border": "$inputFocusBorder",
            "input-focus-outline": "$inputFocusOutline",
            "input-error-border": "$inputErrorBorder",
            "input-error-background": "$inputErrorBackground",
            "input-success-border": "$inputSuccessBorder",
            "input-success-background": "$inputSuccessBackground",
            "button-primary-background": "$buttonPrimaryBg",
            "button-primary-hover": "$buttonPrimaryHover",
            "button-primary-active": "$buttonPrimaryActive",
            "button-primary-text": "$buttonPrimaryText",
            "button-secondary-background": "$buttonSecondaryBg",
            "button-secondary-hover": "$buttonSecondaryHover",
            "button-secondary-active": "$buttonSecondaryActive",
            "button-secondary-text": "$buttonSecondaryText",
            "button-disabled-background": "$buttonDisabledBg",
            "button-disabled-text": "$buttonDisabledText",
        },
        
        # Navigation element styling variables
        "Navigation": {
            "nav-background": "$navBackground",
            "nav-item-color": "$navItemColor",
            "nav-item-hover": "$navItemHover",
            "nav-item-active": "$navItemActive",
            "nav-item-active-background": "$navItemActiveBg",
            "nav-border": "$navBorder",
            "nav-shadow": "0 2px 4px $navShadowColor",
            "nav-mobile-background": "$navMobileBg",
            "nav-icon-color": "$navIconColor",
            "nav-icon-active": "$navIconActive",
            "sidebar-background": "$sidebarBg",
            "sidebar-item-color": "$sidebarItemColor",
            "sidebar-item-hover": "$sidebarItemHover",
            "sidebar-item-active": "$sidebarItemActive",
            "sidebar-item-active-background": "$sidebarItemActiveBg",
            "sidebar-border": "$sidebarBorder",
        },
        
        # Status and notification variables
        "Statuses": {
            "success-background": "$successBackground",
            "success-text": "$successText",
            "success-border": "$successBorder",
            "success-light-background": "$successLightBg",
            "error-background": "$errorBackground",
            "error-text": "$errorText",
            "error-border": "$errorBorder",
            "error-light-background": "$errorLightBg",
            "warning-background": "$warningBackground",
            "warning-text": "$warningText",
            "warning-border": "$warningBorder",
            "warning-light-background": "$warningLightBg",
            "info-background": "$infoBackground",
            "info-text": "$infoText",
            "info-border": "$infoBorder",
            "info-light-background": "$infoLightBg",
            "neutral-background": "$neutralBackground",
            "neutral-text": "$neutralText",
            "neutral-border": "$neutralBorder",
            "neutral-light-background": "$neutralLightBg",
        },
        
        # Table element styling variables
        "Tables": {
            "table-header-background": "$tableHeaderBg",
            "table-header-text": "$tableHeaderText",
            "table-row-background": "$tableRowBg",
            "table-row-background-alt": "$tableRowAltBg",
            "table-row-hover": "$tableRowHover",
            "table-row-active": "$tableRowActive",
            "table-border": "$tableBorder",
            "table-text": "$tableText",
            "table-text-secondary": "$tableTextSecondary",
            "table-footer-background": "$tableFooterBg",
            "table-caption": "$tableCaption",
        },
        
        # Layout structural variables
        "Layout": {
            "spacing-xxsmall": "0.25rem",  # Non-color values remain as fixed values
            "spacing-xsmall": "0.5rem",
            "spacing-small": "0.75rem",
            "spacing-medium": "1rem",
            "spacing-large": "1.5rem",
            "spacing-xlarge": "2rem",
            "spacing-xxlarge": "3rem",
            "spacing-xxxlarge": "4rem",
            "breakpoint-small": "30em",
            "breakpoint-medium": "48em",
            "breakpoint-large": "62em",
            "breakpoint-xlarge": "80em",
            "breakpoint-xxlarge": "96em",
            "max-width-small": "30rem",
            "max-width-medium": "48rem",
            "max-width-large": "62rem",
            "max-width-xlarge": "80rem",
            "max-width-xxlarge": "96rem",
        },
        
        # Typography variables
        "Typography": {
            "font-family-base": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
            "font-family-heading": "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
            "font-family-mono": "'Roboto Mono', 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace",
            "font-size-xxsmall": "0.625rem",
            "font-size-xsmall": "0.75rem",
            "font-size-small": "0.875rem",
            "font-size-medium": "1rem",
            "font-size-large": "1.125rem",
            "font-size-xlarge": "1.25rem",
            "font-size-xxlarge": "1.5rem",
            "font-size-xxxlarge": "1.875rem",
            "font-size-xxxxlarge": "2.25rem",
            "font-weight-light": "300",
            "font-weight-normal": "400",
            "font-weight-medium": "500",
            "font-weight-semibold": "600",
            "font-weight-bold": "700",
            "line-height-tight": "1.25",
            "line-height-normal": "1.5",
            "line-height-loose": "2",
        },
        
        # Animation and transition variables
        "Animation": {
            "duration-instant": "0ms",
            "duration-xxfast": "50ms",
            "duration-xfast": "100ms",
            "duration-fast": "150ms",
            "duration-normal": "200ms",
            "duration-slow": "300ms",
            "duration-xslow": "500ms",
            "duration-xxslow": "750ms",
            "easing-linear": "linear",
            "easing-ease": "ease",
            "easing-ease-in": "ease-in",
            "easing-ease-out": "ease-out",
            "easing-ease-in-out": "ease-in-out",
        },
        
        # Content area variables
        "Content": {
            "content-background": "$contentBg",
            "content-text": "$contentText",
            "content-text-secondary": "$contentTextSecondary",
            "content-link": "$contentLink",
            "content-link-hover": "$contentLinkHover",
            "content-border": "$contentBorder",
            "content-heading-color": "$contentHeading",
            "content-code-background": "$contentCodeBg",
            "content-code-text": "$contentCodeText",
            "content-blockquote-border": "$contentBlockquoteBorder",
            "content-blockquote-background": "$contentBlockquoteBg",
            "content-blockquote-text": "$contentBlockquoteText",
            "content-table-header-bg": "$contentTableHeaderBg",
            "content-table-header-text": "$contentTableHeaderText",
            "content-table-border": "$contentTableBorder",
        },
    }
```

## Integration with Textual Implementation

To integrate this UTTER format with our Textual implementation, we'll add export functionality to our palette management system:

```python
# milky_suite/utils/export_utils.py
from milky_suite.utils.utter import UTTER

def export_palette_to_utter(palette_data):
    """
    Export a palette to the UTTER format.
    
    Args:
        palette_data (dict): Dictionary containing palette colors
            e.g. {'colors': ['#FF5500', '#333333', ...], 'name': 'My Palette'}
    
    Returns:
        dict: UTTER export data containing the formatted output
    """
    # Map palette colors to expected UTTER input format
    colors = palette_data.get('colors', [])
    
    # Create a dictionary of color references for UTTER
    color_mapping = {
        'primary': colors[0] if len(colors) > 0 else '#000000',
        'secondary': colors[1] if len(colors) > 1 else '#000000',
        'tertiary': colors[2] if len(colors) > 2 else '#000000',
        'dark': colors[3] if len(colors) > 3 else '#000000',
        'light': colors[4] if len(colors) > 4 else '#FFFFFF',
        'accent': colors[5] if len(colors) > 5 else '#000000',
        'altBackground': colors[6] if len(colors) > 6 else '#000000',
        'textPrimary': colors[7] if len(colors) > 7 else '#000000',
    }
    
    # Add auto-generated derivatives
    color_mapping.update({
        'hoverBackground': color_mapping['primary'] + '22',  # Add alpha for hover state
        'activeBackground': color_mapping['primary'] + 'aa',  # Add alpha for active state
        'disabledBackground': '#CCCCCC',
        'cardBackground': color_mapping['light'],
        'modalBackground': color_mapping['light'],
        'dropdownBackground': color_mapping['light'],
        'tooltipBackground': color_mapping['dark'],
        'insetBackground': color_mapping['light'] + '88',
        'elevatedBackground': color_mapping['light'],
        'sunkenBackground': color_mapping['light'] + 'dd',
        'textSecondary': color_mapping['dark'],
        'textTertiary': color_mapping['dark'] + '88',
        'textMuted': color_mapping['dark'] + '66',
        'textDisabled': color_mapping['dark'] + '44',
        'textInverse': color_mapping['light'],
        'linkColor': color_mapping['primary'],
        'linkHoverColor': color_mapping['secondary'],
        'borderColor': color_mapping['dark'] + '33',
        'borderColorLight': color_mapping['dark'] + '11',
        'borderColorDark': color_mapping['dark'] + '55',
        'borderColorAccent': color_mapping['primary'],
        'borderColorFocus': color_mapping['primary'] + '88',
        # Add more derivatives as needed
    })
    
    # Create UTTER instance with our color mapping
    utter_instance = UTTER.create_from_palette(color_mapping)
    
    # Return the export data
    return {
        'name': palette_data.get('name', 'Untitled Palette'),
        'content': utter_instance.to_css(),
        'raw': utter_instance.to_dict(),
        'json': utter_instance.to_json(),
    }
```

## Usage in the Textual Application

```python
# Example usage in the ExportPanel widget
def on_export_button_pressed(self):
    """Handle export button press."""
    # Get the active palette from our model
    active_palette = self.app.palette_model.get_active_palette()
    
    # Export using the UTTER format
    export_data = export_palette_to_utter(active_palette)
    
    # Display the exported content
    self.query_one("#export-content").update(export_data['content'])
    
    # Save to clipboard if requested
    if self.export_format == "utter":
        # ...handle clipboard logic
        pass
```

## Differences from CoffeeScript Implementation

1. **Class-based Structure**: Python implementation uses a class with class methods, instance methods, and class variables, rather than the object-with-methods approach in CoffeeScript.

2. **Naming Conventions**: Following Python conventions with snake_case for method names and parameters, while preserving camelCase for the actual CSS variable names to ensure compatibility with CSS standards.

3. **Additional Methods**: Added `to_dict()` and `to_json()` methods for more flexible export options.

4. **Type Hints**: Would normally include Python type hints, but omitted here for brevity.

5. **Default Values**: More robust handling of default values and missing colors.

## Textual-Specific Enhancements

1. **Rich Integration**: The UTTER system can be integrated with Rich's syntax highlighting for displaying the generated CSS in the terminal.

2. **Reactive Properties**: When integrated into a Textual application, reactive variables can be used to automatically update the preview when colors change.

3. **Message System**: Export actions will use Textual's message system to communicate between components.

4. **Widget Rendering**: The exported UTTER format can be rendered in a custom widget with syntax highlighting and copy functionality.

## Conclusion

This Python implementation of the UTTER format maintains all the functionality of the original CoffeeScript version while adapting it to Python's idioms and integrating with the Textual framework. It provides a clean, object-oriented approach to managing color palettes and exporting them in various formats.

The implementation is designed to be flexible and extensible, allowing for additional export formats and customizations in the future. It also integrates well with Textual's reactive programming model, ensuring that changes to the palette are immediately reflected in the export preview.
