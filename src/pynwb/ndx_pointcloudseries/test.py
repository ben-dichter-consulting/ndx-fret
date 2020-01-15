from datetime import datetime
from pynwb import NWBFile, NWBHDF5IO
from ndx_fretcloudseries import FRETSeries

nwb = NWBFile('session_description', 'identifier', datetime.now().astimezone())

# Write nwb file
with NWBHDF5IO('test_fretseries.nwb', 'w') as io:
    io.write(nwb)

# Read nwb file and check its content
with NWBHDF5IO('test_fretseries.nwb', 'r', load_namespaces=True) as io:
    nwb = io.read()
    print(nwb)
