from mcp.server.fastmcp import FastMCP

# Create the MCP server instance
mcp = FastMCP("calculator-server")


# ─── TOOL 1: add ────────────────────────────────────────────
# This tool is COMPLETE — study this pattern carefully
@mcp.tool()
def add(a: float, b: float) -> str:
    """Add two numbers together."""
    result = a + b
    return f"{a} + {b} = {result}"


@mcp.tool()
def multiply(a: float, b: float) -> str:
    """Multiply two numbers together."""
    result = a * b
    return f"{a} × {b} = {result}"

