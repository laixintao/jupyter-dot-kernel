# -*- coding: utf-8 -*-
import base64
import urllib
from . import imgsize
from graphviz import Source

from ipykernel.kernelbase import Kernel


class EchoKernel(Kernel):
    implementation = "Echo"
    implementation_version = "1.0"
    language = "no-op"
    language_version = "0.1"
    language_info = {
        "name": "Any text",
        "mimetype": "text/plain",
        "file_extension": ".txt",
    }
    banner = "Echo kernel - as useful as a parrot"

    def do_execute(
        self, code, silent, store_history=True,
        user_expressions=None, allow_stdin=False
    ):
        src = Source(code)
        png_src = src.pipe(format="png")
        if not silent:
            data = urllib.parse.quote(base64.b64encode(png_src))
            width, height = imgsize.get_png_size(png_src)
            stream_content = {
                "metadata": {"image/png": {"width": width, "height": height}},
                "data": {"image/png": data},
            }

            self.send_response(self.iopub_socket, "display_data", stream_content)

        return {
            "status": "ok",
            # The base class increments the execution count
            "execution_count": self.execution_count,
            "payload": [],
            "user_expressions": {},
        }
