#
# Copyright(c) 2019 Intel Corporation
# SPDX-License-Identifier: BSD-3-Clause-Clear
#
from storage_devices.disk import Disk, DiskType


class Dut:
    def __init__(self, dut_info):
        self.ip = dut_info['ip']
        self.disks = []
        for disk_info in dut_info['disks']:
            self.disks.append(Disk(disk_info['path'],
                                   DiskType[disk_info['type']],
                                   disk_info['serial'],
                                   disk_info['blocksize']))

        self.ipmi = dut_info['ipmi'] if 'ipmi' in dut_info else None
        self.spider = dut_info['spider'] if 'spider' in dut_info else None
        self.wps = dut_info['wps'] if 'wps' in dut_info else None

    def __str__(self):
        dut_str = f'ip: {self.ip}\n'
        dut_str += f'ipmi: {self.ipmi}\n' if self.ipmi is not None else ''
        dut_str += f'spider: {self.spider}\n' if self.spider is not None else ''
        dut_str += f'wps: {self.wps}\n' if self.wps is not None else ''
        dut_str += f'disks:\n'
        for disk in self.disks:
            dut_str += f"\t{disk}"
        dut_str += "\n"
        return dut_str