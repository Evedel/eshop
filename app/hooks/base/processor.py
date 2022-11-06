class OSWrapper:  # pragma: no cover
    def sh(self, command: str) -> None:
        import os

        os.system(command)

    def env(self, key: str) -> str:
        import os

        return os.environ[key]


class SysWrapper:  # pragma: no cover
    def is_config(self) -> None:
        import sys

        return len(sys.argv) > 1 and sys.argv[1] == "--config"


class PrintWrapper:  # pragma: no cover
    def print(self, message: str) -> None:
        print(message)


class JsonWrapper:  # pragma: no cover
    def json_load(self, path: str) -> dict:
        import json

        context = json.load(open(path))
        print(context)
        return context


class HookProcessor:
    def __init__(
        self,
        os: OSWrapper = OSWrapper(),
        sys: SysWrapper = SysWrapper(),
        print: PrintWrapper = PrintWrapper(),
        json: JsonWrapper = JsonWrapper(),
    ):
        self.__sh = os.sh
        self.__is_config = sys.is_config
        self.__print = print.print
        self.__json_load = json.json_load
        self.__env = os.env

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
