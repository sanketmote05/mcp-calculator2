from mcp.server.fastmcp import FastMCP

mcp = FastMCP("calculator")


@mcp.tool()
def add(a: float, b: float) -> float:
    return a + b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    return a * b


def main():
    mcp.run()


if __name__ == "__main__":
    main()
