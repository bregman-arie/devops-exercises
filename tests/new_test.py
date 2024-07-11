import pytest
from unittest.mock import MagicMock
from pluggy import PluginManager, PluginValidationError

@pytest.fixture
def plugin_manager():
    return PluginManager("test_project")

def test_unregister(plugin_manager):
    class Plugin:
        pass

    plugin = Plugin()
    plugin_manager.register(plugin, "test_plugin")

    hook_caller = MagicMock()
    plugin_manager.hook.test_hook = hook_caller
    hook_caller.get_hookimpls.return_value = [MagicMock(plugin=plugin)]
    
    plugin_manager.unregister(plugin=plugin)
    hook_caller._remove_plugin.assert_called_once_with(plugin)
    
    plugin_manager.register(plugin, "test_plugin")
    plugin_manager.set_blocked("test_plugin")
    unregistered_plugin = plugin_manager.unregister(name="test_plugin")
    
    assert unregistered_plugin is None
    assert not plugin_manager.is_registered(plugin)

def test_check_pending(plugin_manager):
    class Plugin:
        pass

    plugin = Plugin()
    plugin_manager.register(plugin, "test_plugin")

    hook_caller = MagicMock()
    hook_caller.has_spec.return_value = False
    hook_impl = MagicMock(optionalhook=False, plugin=plugin)
    hook_caller.get_hookimpls.return_value = [hook_impl]
    plugin_manager.hook.test_hook = hook_caller

    with pytest.raises(PluginValidationError, match="unknown hook"):
        plugin_manager.check_pending()