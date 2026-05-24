from mcp.server.fastmcp import FastMCP
import os
import random

mcp = FastMCP(
    "saad-test-mcp-server",
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 3000)),
)

@mcp.tool()
def add(a: float, b: float) -> float:
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@mcp.tool()
def reverse_string(s: str) -> str:
    return s[::-1]

@mcp.tool()
def count_words(s: str) -> int:
    return len(s.split())

@mcp.tool()
def random_joke() -> str:
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "A SQL query walks into a bar and asks two tables: 'Can I join you?'",
    ]
    return random.choice(jokes)

if __name__ == "__main__":
    mcp.run(transport="streamable-http")