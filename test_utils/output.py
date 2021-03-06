#
# Copyright(c) 2019 Intel Corporation
# SPDX-License-Identifier: BSD-3-Clause-Clear
#


class Output:
    def __init__(self, output_out, output_err, return_code):
        self.stdout = output_out.decode('utf-8').rstrip() if type(output_out) == bytes else \
            output_out
        self.stderr = output_err.decode('utf-8').rstrip() if type(output_err) == bytes else \
            output_err
        self.exit_code = return_code

    def __str__(self):
        return f"stdout: {self.stdout}\nstderr: {self.stderr}"


class CmdException(Exception):
    def __init__(self, message: str, output: Output):
        super().__init__(f"{message}\n{str(output)}")
        self.output = output
