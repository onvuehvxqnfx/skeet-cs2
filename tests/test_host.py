from skeet.host import PluginHost
from skeet.loader import load_builtin_plugins


def test_host_registers_builtin_plugins():
    host = PluginHost()
    load_builtin_plugins(host)
    assert "entity_walker" in host.registry
    assert "netvar_dumper" in host.registry


def test_host_runs_dump():
    host = PluginHost()
    load_builtin_plugins(host)
    results = host.run(build="2401")
    assert results["entity_walker"]["count"] == 64