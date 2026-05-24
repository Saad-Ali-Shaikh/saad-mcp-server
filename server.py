from mcp.server.fastmcp import FastMCP
import os
import random

mcp = FastMCP(
    "saad-test-mcp-server",
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 3000)),
    streamable_http_path="/mcp",
)

if hasattr(mcp.settings, "transport_security"):
    mcp.settings.transport_security.enable_dns_rebinding_protection = False


@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together"""
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract two numbers"""
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


@mcp.tool()
def reverse_string(s: str) -> str:
    """Reverse a string"""
    return s[::-1]


@mcp.tool()
def count_words(s: str) -> int:
    """Count words in a string"""
    return len(s.split())


@mcp.tool()
def random_joke() -> str:
    """Get a random programming joke"""
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "A SQL query walks into a bar and asks two tables: 'Can I join you?'",
        "Why did the developer go broke? He used up all his cache.",
        "How many programmers to change a lightbulb? None — that's a hardware problem.",
        "Why do Java developers wear glasses? Because they don't C#.",
    ]
    return random.choice(jokes)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")