class StdLibWrapper:  # pragma: no cover
    def sh(self, command: str) -> None:
        import subprocess

        if subprocess.run(command).returncode != 0:
            raise Exception(f"command failed: {command}")

    def env(self, key: str) -> str:
        import os

        return os.environ[key]

    def is_config(self) -> bool:
        import sys

        return len(sys.argv) > 1 and sys.argv[1] == "--config"

    def json_load(self, path: str) -> dict:
        import json

        context = json.load(open(path))
        print(context)
        return context

    def print(self, message: str) -> None:
        print(message)


class HookProcessor:
    def __init__(
        self,
        std_lib: StdLibWrapper = StdLibWrapper(),
    ):
        self.__sh = std_lib.sh
        self.__is_config = std_lib.is_config
        self.__print = std_lib.print
        self.__json_load = std_lib.json_load
        self.__env = std_lib.env

    def __on_synchronization(self, context: dict, entrypoint: str) -> None:
        for obj in context["objects"]:
            namespace = obj["object"]["metadata"]["namespace"]
            name = obj["object"]["metadata"]["name"]
            self.__print(f"--- Synchronization {namespace} {name}")
            self.__sh(f"{entrypoint} {namespace} {name}")

    def __on_event(self, context: dict, entrypoint: str) -> None:
        namespace = context["object"]["metadata"]["namespace"]
        name = context["object"]["metadata"]["name"]
        self.__print(f"--- Event {namespace} {name}")
        self.__sh(f"{entrypoint} {namespace} {name}")

    def execute(self, config, entrypoint) -> None:
        """
        assumption: all filtering is happening in the hook configuration

        return "config" if "--config" is passed

        else, run "entrypoint" script for each object in the context
        (both synchronization and event)
        """
        if self.__is_config():
            self.__print(config)
        else:
            context_path = self.__env("BINDING_CONTEXT_PATH")
            context = self.__json_load(context_path)
            for task in context:
                if task["type"] == "Synchronization":
                    self.__on_synchronization(task, entrypoint)
                elif task["type"] == "Event":
                    self.__on_event(task, entrypoint)
                else:
                    raise Exception(f"Unknown task type '{task['type']}'")
