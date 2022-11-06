import unittest
from unittest.mock import MagicMock

from hooks.base.processor import (
    HookProcessor,
    JsonWrapper,
    OSWrapper,
    PrintWrapper,
    SysWrapper,
)


class TestHookProcessor(unittest.TestCase):
    def test_execute_when_config_called(self):
        # Arrange
        config = "test-config"
        entrypoint = "test-entrypoint"

        sys_wrapper = MagicMock(spec_set=SysWrapper)
        print_wrapper = MagicMock(spec_set=PrintWrapper)

        sys_wrapper.is_config.return_value = True

        hook_processor = HookProcessor(sys=sys_wrapper, print=print_wrapper)

        # Act
        hook_processor.execute(config, entrypoint)

        # Assert
        print_wrapper.print.assert_called_once_with(config)

    def test_execute_when_unknown_context_type(self):
        # Arrange
        config = "test-config"
        entrypoint = "test-entrypoint"

        sys_wrapper = MagicMock(spec_set=SysWrapper)
        json_wrapper = MagicMock(spec_set=JsonWrapper)

        sys_wrapper.is_config.return_value = False
        context = self.__get_context_synchronization()
        context[0]["type"] = "Unknown"
        json_wrapper.json_load.return_value = context

        hook_processor = HookProcessor(
            sys=sys_wrapper,
            json=json_wrapper,
        )

        # Assert (# Act)
        self.assertRaises(Exception, hook_processor.execute, config, entrypoint)

    def test_execute_when_synchronization_no_objects(self):
        # Arrange
        config = "test-config"
        entrypoint = "test-entrypoint"

        sys_wrapper = MagicMock(spec_set=SysWrapper)
        json_wrapper = MagicMock(spec_set=JsonWrapper)
        os_wrapper = MagicMock(spec_set=OSWrapper)

        sys_wrapper.is_config.return_value = False
        context = self.__get_context_synchronization()
        context[0]["objects"] = []
        json_wrapper.json_load.return_value = context

        hook_processor = HookProcessor(
            sys=sys_wrapper,
            json=json_wrapper,
            os=os_wrapper,
        )

        # Act
        hook_processor.execute(config, entrypoint)

        # Assert
        os_wrapper.sh.assert_not_called()

    def test_execute_when_synchronization_multiple_objects(self):
        # Arrange
        config = "test-config"
        entrypoint = "/app/test-entrypoint/script"

        sys_wrapper = MagicMock(spec_set=SysWrapper)
        json_wrapper = MagicMock(spec_set=JsonWrapper)
        os_wrapper = MagicMock(spec_set=OSWrapper)
        print_wrapper = MagicMock(spec_set=PrintWrapper)

        sys_wrapper.is_config.return_value = False
        context = self.__get_context_synchronization()
        context[0]["objects"][0]["object"]["metadata"]["namespace"] = "test-namespace-1"
        context[0]["objects"][0]["object"]["metadata"]["name"] = "test-object-1"
        context[0]["objects"][1]["object"]["metadata"]["namespace"] = "test-namespace-1"
        context[0]["objects"][1]["object"]["metadata"]["name"] = "test-object-2"
        context[0]["objects"][2]["object"]["metadata"]["namespace"] = "test-namespace-2"
        context[0]["objects"][2]["object"]["metadata"]["name"] = "test-object-3"
        json_wrapper.json_load.return_value = context

        hook_processor = HookProcessor(
            sys=sys_wrapper,
            json=json_wrapper,
            os=os_wrapper,
            print=print_wrapper,
        )

        # Act
        hook_processor.execute(config, entrypoint)

        # Assert
        def gen_sh_call(namespace: str, name: str) -> unittest.mock.call:
            return unittest.mock.call(f"{entrypoint} {namespace} {name}")

        def gen_print_call(namespace: str, name: str) -> unittest.mock.call:
            return unittest.mock.call(f"--- Synchronization {namespace} {name}")

        self.assertEqual(3, os_wrapper.sh.call_count)
        os_wrapper.sh.assert_has_calls(
            [
                gen_sh_call("test-namespace-1", "test-object-1"),
                gen_sh_call("test-namespace-1", "test-object-2"),
                gen_sh_call("test-namespace-2", "test-object-3"),
            ]
        )

        self.assertEqual(3, print_wrapper.print.call_count)
        print_wrapper.print.assert_has_calls(
            [
                gen_print_call("test-namespace-1", "test-object-1"),
                gen_print_call("test-namespace-1", "test-object-2"),
                gen_print_call("test-namespace-2", "test-object-3"),
            ]
        )

    def test_execute_when_single_event(self):
        # Arrange
        config = "test-config"
        entrypoint = "/app/test-entrypoint/script"

        sys_wrapper = MagicMock(spec_set=SysWrapper)
        json_wrapper = MagicMock(spec_set=JsonWrapper)
        os_wrapper = MagicMock(spec_set=OSWrapper)
        print_wrapper = MagicMock(spec_set=PrintWrapper)

        sys_wrapper.is_config.return_value = False
        context = self.__get_context_event_single()
        context[0]["object"]["metadata"]["namespace"] = "test-namespace-1"
        context[0]["object"]["metadata"]["name"] = "test-object-1"
        json_wrapper.json_load.return_value = context

        hook_processor = HookProcessor(
            sys=sys_wrapper,
            json=json_wrapper,
            os=os_wrapper,
            print=print_wrapper,
        )

        # Act
        hook_processor.execute(config, entrypoint)

        # Assert
        os_wrapper.sh.assert_has_calls(
            [
                unittest.mock.call(
                    "/app/test-entrypoint/script test-namespace-1 test-object-1"
                ),
            ]
        )

        print_wrapper.print.assert_has_calls(
            [
                unittest.mock.call("--- Event test-namespace-1 test-object-1"),
            ]
        )

    def test_execute_when_grouped_events(self):
        # Arrange
        config = "test-config"
        entrypoint = "/app/test-entrypoint/script"

        sys_wrapper = MagicMock(spec_set=SysWrapper)
        json_wrapper = MagicMock(spec_set=JsonWrapper)
        os_wrapper = MagicMock(spec_set=OSWrapper)
        print_wrapper = MagicMock(spec_set=PrintWrapper)

        sys_wrapper.is_config.return_value = False
        context = self.__get_context_event_multiple()
        context[0]["object"]["metadata"]["namespace"] = "test-namespace-1"
        context[0]["object"]["metadata"]["name"] = "test-object-1"
        context[1]["object"]["metadata"]["namespace"] = "test-namespace-2"
        context[1]["object"]["metadata"]["name"] = "test-object-2"
        context[2]["object"]["metadata"]["namespace"] = "test-namespace-1"
        context[2]["object"]["metadata"]["name"] = "test-object-2"
        json_wrapper.json_load.return_value = context

        hook_processor = HookProcessor(
            sys=sys_wrapper,
            json=json_wrapper,
            os=os_wrapper,
            print=print_wrapper,
        )

        # Act
        hook_processor.execute(config, entrypoint)

        # Assert
        def gen_sh_call(namespace: str, name: str) -> unittest.mock.call:
            return unittest.mock.call(f"{entrypoint} {namespace} {name}")

        def gen_print_call(namespace: str, name: str) -> unittest.mock.call:
            return unittest.mock.call(f"--- Event {namespace} {name}")

        self.assertEqual(3, os_wrapper.sh.call_count)
        os_wrapper.sh.assert_has_calls(
            [
                gen_sh_call("test-namespace-1", "test-object-1"),
                gen_sh_call("test-namespace-2", "test-object-2"),
                gen_sh_call("test-namespace-1", "test-object-2"),
            ]
        )

        self.assertEqual(3, print_wrapper.print.call_count)
        print_wrapper.print.assert_has_calls(
            [
                gen_print_call("test-namespace-1", "test-object-1"),
                gen_print_call("test-namespace-2", "test-object-2"),
                gen_print_call("test-namespace-1", "test-object-2"),
            ]
        )

    def __get_context_synchronization(self):
        # https://github.com/flant/shell-operator/blob/main/HOOKS.md#synchronization-binding-context
        from hooks.test.contexts import SYNCHRONISATION

        return SYNCHRONISATION

    def __get_context_event_single(self):
        # https://github.com/flant/shell-operator/blob/main/HOOKS.md#event-binding-context
        from hooks.test.contexts import EVENT_SINGLE

        return EVENT_SINGLE

    def __get_context_event_multiple(self):
        # https://github.com/flant/shell-operator/blob/main/HOOKS.md#event-binding-context
        from hooks.test.contexts import EVENT_MULTIPLE

        return EVENT_MULTIPLE
