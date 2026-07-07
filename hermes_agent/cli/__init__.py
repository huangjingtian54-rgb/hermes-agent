"""
Hermes Agent CLI entry point.
"""

import sys
import fire


def main():
    """Entry point for Hermes Agent CLI."""
    from hermes_agent.cli import cli
    fire.cli(cli)


def main():
    """Entry point for Hermes Agent CLI."""
    import sys
    from hermes_agent.cli import run
    return run()


if __name__ == "__main__":
    main()
