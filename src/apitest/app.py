import sys
import subprocess as sp
from collections import namedtuple

RunMode = namedtuple("Mode", ["cmd", "opts", "args"])


class ModeMaster:
    def __init__(self, modes, default_cmd):
        self.modes = modes
        self.default_cmd = default_cmd

    def build_cmd(self, mode):
        cmd = [self.modes[mode].cmd]
        if self.modes[mode].opts is not None:
            for opt in self.modes[mode].opts.items():
                cmd.extend(opt)
        cmd.extend(self.modes[mode].args)
        return cmd

    def run_mode(self, mode=None):
        if mode is not None:
            sp.run(self.build_cmd(mode))
        else:
            sp.run(self.build_cmd(self.default_cmd))


run_modes = {
    "service": RunMode(
        cmd="gunicorn",
        opts={
            "-b": "0.0.0.0:8008",
            "-w": "1",
        },
        args=[
            "apitest.core:app"
        ],
    ),
    "hello": RunMode(
        cmd="echo",
        opts = None,
        args = ["Hello, World!"],
    )
}

default_mode = "service"

runner = ModeMaster(run_modes, default_mode)

if len(sys.argv) > 1:
    runner.run_mode(sys.argv[1])
else:
    runner.run_mode()
