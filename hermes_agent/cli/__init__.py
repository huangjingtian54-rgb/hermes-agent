"""
Hermes Agent CLI entry point.
"""

import json
import sys


def main(argv=None) -> int:
    """Entry point for Hermes Agent CLI."""
    from hermes_agent.scripts import chat, cron, memory, run, setup, skills, tools

    args = list(sys.argv[1:] if argv is None else argv)
    command = args[0] if args else "help"

    if command in {"--version", "-V"}:
        from hermes_agent.__version__ import __version__

        print(__version__)
        return 0

    if command in {"run", "--session", "-s"}:
        prompt = args[1] if len(args) > 1 else ""
        result = run(prompt)
        print(json.dumps(result))
        return 0

    if command in {"chat", "-c", "--chat"}:
        prompt = args[1] if len(args) > 1 else ""
        result = chat(prompt)
        print(json.dumps(result))
        return 0

    if command == "setup":
        result = setup()
        print(json.dumps(result))
        return 0

    if command == "config":
        config_args = {}
        if len(args) > 2 and args[1] == "set":
            config_args["set"] = args[2]
        elif len(args) > 2 and args[1] == "get":
            config_args["get"] = args[2]
        from hermes_agent.scripts import config as config_cmd

        config_cmd(**config_args)
        return 0

    if command == "skills":
        if len(args) > 2 and args[1] == "view":
            skills(view=args[2])
        elif len(args) > 2 and args[1] == "create":
            skills(create=args[2])
        else:
            skills()
        return 0

    if command == "cron":
        cron()
        return 0

    if command == "tools":
        tools()
        return 0

    if command == "memory":
        memory()
        return 0

    print("Usage: hermes <run|chat|setup|config|skills|cron|tools|memory|--version>")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
