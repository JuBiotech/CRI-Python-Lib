# Introduction 
Python package to interface an igus Robot Control via the CRI protocol.

# Current Features
- Robot State
- Basic functions
    - Reset
    - Enable / Disable
    - Acquisition of active control
    - Override
- Referencing of 
    - single axis
    - all axes
    - Set joints to zero
- Direct movements
    - Joint and relative joint
    - Cartesian
    - Cartesian base and tool relative
- Live jog
- Digital IO and global signals
- Programs
    - Upload
    - Start / Pause / Stop
- CAN Bridge

# Getting Started
## Installation
Using the library requires no additional libraries, only testing has external dependencies.

In the top directory of this repository execute `pip install .`

## Examples
See `examples` directory.

# Tests
This repository provides pytests for the message parser. They require `pytest` and `pytest-cov`, which can be installed via `pip install -r requirements.txt`. To run the tests (including coverage) execute the following command: `pytest -vv --cov=cri_lib --cov-report term-missing tests`. 

