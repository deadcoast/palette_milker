# Palette Milker Test Suite

This directory contains the tests for the Palette Milker application.

The test suite uses pytest for testing and pytest-cov for coverage reporting.

## Running Tests

To run all tests:

```bash
pytest
```

To run tests with coverage:

```bash
pytest --cov=src
```

To run a specific test file:

```bash
pytest tests/test_color_utils.py
```

To run a specific test:

```bash
pytest tests/test_color_utils.py::TestGenerateHarmonicPalette::test_complementary_palette
```

## Test Files

### Core Models

- `test_color_model.py` - Tests for the Color class and related functionality
- `test_palette_model.py` - Tests for Palette, PaletteCollection, and PaletteModel classes
- `test_application_state.py` - Tests for application state management

### Utilities

- `test_color_utils.py` - Tests for color manipulation and generation utilities
- `test_export_utils.py` - Tests for palette exporting in various formats
- `test_serialization.py` - Tests for palette serialization, saving, and loading
- `test_error_handler.py` - Tests for error handling and notification functionality

### UI Components

- `test_widgets.py` - Basic tests for Textual UI widgets

## Test Coverage

The test suite aims to achieve high coverage of the codebase, especially for the model and utility classes.

Current coverage:
- `src/utils/color_utils.py`: 72%
- `src/utils/error_handler.py`: 90%
- `src/utils/export_utils.py`: 99%
- `src/models/application_state.py`: 79%
- `src/models/color_model.py`: 70%
- `src/models/palette_model.py`: 82%

## Testing Approach

- **Unit Tests**: Most tests are unit tests that isolate and test specific components.
- **Mocking**: Extensive use of `unittest.mock` to mock dependencies and test components in isolation.
- **Fixtures**: Pytest fixtures are used to provide test data and mock objects.
- **Parametrization**: Where appropriate, tests are parametrized to test multiple scenarios.

### Textual UI Testing Limitations

Testing Textual UI components presents challenges as they're designed to run within a Textual app context. The `test_widgets.py` file contains simplified tests that verify basic properties without attempting to mount or interact with widgets in a full app context.

For fully interactive UI testing, the Textual framework provides the `pilot` module, which is not used in this test suite.

## Adding Tests

When adding new tests:
1. Follow the existing patterns for similar components
2. Include docstrings explaining what each test is verifying
3. Use type hints for all parameters and return values
4. Keep tests focused on specific functionality
5. Use fixtures to reduce code duplication
6. Mock external dependencies to keep tests fast and reliable
