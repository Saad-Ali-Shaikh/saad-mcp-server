from mcp.server.fastmcp import FastMCP
import os

# mcp = FastMCP("saad-test-mcp-server")

mcp = FastMCP(
    "saad-test-mcp-server",
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 3000)),
    streamable_http_path="/mcp",
)

# Disable DNS rebinding protection so Render's hostname is accepted.
# Safe here because the server has no auth and is meant to be publicly reachable.
mcp.settings.transport_security.enable_dns_rebinding_protection = False

@mcp.tool()
def add(a: float, b: float) -> str:
    """Add two numbers together"""
    return f"{a} + {b} = {a + b}"


@mcp.tool()
def subtract(a:float, b: float) -> str:
    """Subtract two numbers together"""
    return f"{a} - {b} = {a - b}"

@mcp.tool()
def multiply(a:float, b: float) -> str:
    """Multiply two numbers together"""
    return f"{a} * {b} = {a * b}"       

@mcp.tool()
def divide(a:float, b: float) -> str:
    """Divide two numbers together"""
    if b == 0:
        return "Cannot divide by zero"
    return f"{a} / {b} = {a / b}"

@mcp.tool()
def reverse_string(s: str) -> str:
    """Reverse a string"""
    return s[::-1]  

@mcp.tool()
def count_words(s: str) -> str:
    """Count the number of words in a string"""
    return f"The number of words in '{s}' is {len(s.split())}"

@mcp.tool()
def random_joke() -> str:
    """Get a random programming joke"""
    import random
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