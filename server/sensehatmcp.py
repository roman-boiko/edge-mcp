from typing import Any
import sys
import os
from mcp.server.fastmcp import FastMCP

try:
    from sense_hat import SenseHat
except ImportError:
    # Add project root to sys.path to find sense_hat_mock
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    from sense_hat_mock.sense_hat import SenseHat

# Initialize the FastMCP server
mcp = FastMCP("sensehatmcp")

# Initialize the SenseHat
sense = SenseHat()


@mcp.tool()
async def get_temperature() -> float:
    """Get the temperature from the Sense HAT in Celsius."""
    return sense.get_temperature()


@mcp.tool()
async def get_humidity() -> float:
    """Get the humidity from the Sense HAT."""
    return sense.get_humidity()


@mcp.tool()
async def get_pressure() -> float:
    """Get the pressure from the Sense HAT in Millibars"""
    return sense.get_pressure()


@mcp.tool()
async def print_message(
    message: str, text_colour: tuple = (255, 255, 255), back_colour: tuple = (0, 0, 0)
) -> None:
    """Print a message on the Sense HAT LED matrix.
    Args:
        message (str): The message to display.
        text_colour (tuple): The RGB color of the text. Default is white.
        back_colour (tuple): The RGB color of the background. Default is black.
    """
    sense.show_message(message, text_colour=text_colour, back_colour=back_colour)


if __name__ == "__main__":
    # Run the FastMCP server
    mcp.run(transport="stdio")
