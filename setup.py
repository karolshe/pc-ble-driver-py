#
# Copyright (c) 2016-2019 Nordic Semiconductor ASA
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#   1. Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
#   2. Redistributions in binary form must reproduce the above copyright notice, this
#   list of conditions and the following disclaimer in the documentation and/or
#   other materials provided with the distribution.
#
#   3. Neither the name of Nordic Semiconductor ASA nor the names of other
#   contributors to this software may be used to endorse or promote products
#   derived from this software without specific prior written permission.
#
#   4. This software must only be used in or with a processor manufactured by Nordic
#   Semiconductor ASA, or in or with a processor manufactured by a third party that
#   is used in combination with a processor manufactured by Nordic Semiconductor.
#
#   5. Any software provided in binary or object form under this license must not be
#   reverse engineered, decompiled, modified and/or disassembled.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
import sys

from skbuild import setup
from setuptools import find_packages

import pc_ble_driver_py

py2 = sys.version_info[0] == 2
py3 = sys.version_info[0] == 3

if py2:
    requirements = ['enum34', 'wrapt', 'future', 'typing']
elif py3:
    requirements = ['wrapt', 'future']

    # Typing is supported from Python 3.5 and onward
    if sys.version_info[1] == 4:
        requirements.append('typing')
else:
    print('pc-ble-driver-py only supports Python version 2 and 3')
    sys.exit(-1)

setup(
    name='pc_ble_driver_py',
    version=pc_ble_driver_py.__version__,
    description='Python bindings for the Nordic pc-ble-driver SoftDevice serialization library',
    long_description='A Python interface and library for pc-ble-driver. This allows Python applications to interface '
                     'with a Nordic Semiconductor IC (both nRF51 and nRF52 series) over a serial port to obtain '
                     'access to the full serialized SoftDevice API.',
    url='https://github.com/NordicSemiconductor/pc-ble-driver-py',
    author='Nordic Semiconductor ASA',
    license='Modified BSD License',
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',

        'Topic :: System :: Networking',
        'Topic :: System :: Hardware :: Hardware Drivers',
        'Topic :: Software Development :: Embedded Systems',

        'License :: Other/Proprietary License',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='nordic nrf51 nrf52 ble bluetooth softdevice serialization bindings pc-ble-driver pc-ble-driver-py '
             'pc_ble_driver pc_ble_driver_py',
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, <4",
    install_requires=requirements,
    packages=find_packages(),
    package_data={
        'pc_ble_driver_py.lib.win.x86_32': ['*.pyd', '*.dll', '*.txt'],
        'pc_ble_driver_py.lib.win.x86_64': ['*.pyd', '*.dll', '*.txt'],
        'pc_ble_driver_py.lib.linux.x86_64': ['*.so', '*.txt'],
        'pc_ble_driver_py.lib.macos_osx': ['*.so', '*.dylib', '*.txt'],
        'pc_ble_driver_py.hex': ['*.hex'],
        'pc_ble_driver_py.hex.sd_api_v2': ['*.hex'],
        'pc_ble_driver_py.hex.sd_api_v5': ['*.hex'],
    }
)
