# Testing the Palette Milker Application

This directory contains tests for the Palette Milker application. The tests are organized into several categories:

1. **Unit Tests**: These test individual components in isolation.
2. **Integration Tests**: These test how components work together.
3. **Widget Tests**: These test Textual widgets and their behavior.

## Requirements

To run the tests, you'll need the following:

- Python 3.8 or newer
- pytest
- pytest-asyncio (for testing Textual apps)
- pytest-mock (for mocking external dependencies)

You can install the required packages with:

```bash
pip install pytest pytest-asyncio pytest-mock
```

## Running the Tests

### Running All Tests

To run all tests, navigate to the project root directory and run:

```bash
python -m pytest tests/
```

### Running Specific Test Files

To run a specific test file:

```bash
python -m pytest tests/test_color_model.py
```

### Running Specific Tests

To run a specific test class or test method:

```bash
# Run a specific test class
python -m pytest tests/test_color_model.py::TestColorModel

# Run a specific test method
python -m pytest tests/test_color_model.py::TestColorModel::test_color_creation_from_hex
```

### Test Verbosity

For more detailed output, use the `-v` (verbose) flag:

```bash
python -m pytest -v tests/
```

To see captured stdout/stderr even for passing tests, use `-s`:

```bash
python -m pytest -s tests/
```

## Test Structure

### Unit Tests

- `test_color_model.py`: Tests for the `Color` class.
- `test_palette_model.py`: Tests for the `Palette` and `PaletteCollection` classes.
- `test_application_state.py`: Tests for the `ApplicationState` class.

### Integration Tests

- `test_widgets.py`: Tests for widgets and their integration with the application.

## Writing New Tests

When writing new tests, follow these guidelines:

1. **Follow the Naming Conventions**: 
   - Test files should be named `test_<module_name>.py`.
   - Test classes should be named `Test<ClassName>`.
   - Test methods should be named `test_<functionality_being_tested>`.

2. **Use Fixtures**: 
   - Use pytest fixtures for setup and teardown.
   - Share fixtures between tests when appropriate.

3. **Mock External Dependencies**:
   - Use `unittest.mock` or `pytest-mock` to mock external dependencies.
   - Avoid tests that require network access or database connections.

4. **Test Both Positive and Negative Cases**:
   - Test expected functionality.
   - Test edge cases and error handling.

5. **Keep Tests Isolated**:
   - Each test should be independent of others.
   - Avoid tests that depend on the order of execution.

## Widget Testing

Testing Textual widgets requires special handling due to their asynchronous nature. We use the Textual Pilot API for this:

```python
@pytest.fixture
def app_runner():
    """Provide a fixture for running textual apps in tests."""
    from textual.pilot import Pilot
    
    async def _app_runner(app_class):
        """Run a Textual app for testing."""
        app = app_class()
        async with Pilot(app) as pilot:
            return pilot
            
    return _app_runner
```

Then in your tests:

```python
async def test_widget_functionality(self, app_runner):
    """Test widget functionality."""
    async with app_runner(self.TestApp) as pilot:
        # Interact with the app
        await pilot.press("a")
        await pilot.click("#button")
        
        # Check the state
        assert pilot.app.widget.value == "expected value"
```

## Continuous Integration

These tests are run automatically in GitHub Actions when changes are pushed to the repository. See the `.github/workflows/tests.yml` file for details. 
