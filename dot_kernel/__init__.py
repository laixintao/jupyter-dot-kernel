# -*- coding: utf-8 -*-
import base64
import urllib

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
        self, code, silent, store_history=True, user_expressions=None, allow_stdin=False
    ):
        if not silent:
            with open("a.png", "rb") as a:
                data = urllib.parse.quote(base64.b64encode(a.read()))
            stream_content = {
                "metadata": {"image/png": {"width": 640, "height": 480}},
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
