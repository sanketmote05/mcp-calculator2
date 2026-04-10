from mcp.server.fastmcp import FastMCP

mcp = FastMCP("calculator-server")

@mcp.tool()
def add(a: float, b: float) -> str:
    """Add two numbers together."""
    result = a + b
    return f"{a} + {b} = {result}"

@mcp.tool()
def multiply(a: float, b: float) -> str:
    """Multiply two numbers together."""
    result = a * b
    return f"{a} x {b} = {result}"

def main():
    mcp.run()
