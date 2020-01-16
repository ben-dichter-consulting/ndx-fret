from pynwb import NWBFile, NWBHDF5IO, ProcessingModule
from pynwb.device import Device
from pynwb.ophys import OpticalChannel
from ndx_fretseries import FRETSeries

from datetime import datetime
import numpy as np

nwb = NWBFile('session_description', 'identifier', datetime.now().astimezone())

# Create and add device
device = Device(name='Device')
nwb.add_device(device)

# Create optical channels
opt_ch_d = OpticalChannel(
    name='OpticalChannel_donor',
    description='',
    emission_lambda=450.
)
opt_ch_a = OpticalChannel(
    name='OpticalChannel_acceptor',
    description='',
    emission_lambda=500.
)

# Ophys processing module
ophys_module = ProcessingModule(
    name='Ophys',
    description='contains optical physiology processed data.',
)
nwb.add_processing_module(ophys_module)

# Create FRET series
data_donor = np.random.randn(100, 10, 10)
data_acceptor = np.random.randn(100, 10, 10)

fret = FRETSeries(
    name='FRETSeries',
    description='',
    excitation_lambda=482.,
    device=device,
    # optical_channel_donor=opt_ch_d,
    # optical_channel_acceptor=opt_ch_a,
    fluorophore_donor='mCitrine',
    fluorophore_acceptor='mKate2',
    data_donor=data_donor,
    data_acceptor=data_acceptor,
    rate=60.,
)

ophys_module.add(fret)
print('--- 1 ---')

# Write nwb file
with NWBHDF5IO('test_fretseries.nwb', 'w') as io:
    io.write(nwb)
    print('--- 2 ---')

# Read nwb file and check its content
with NWBHDF5IO('test_fretseries.nwb', 'r', load_namespaces=True) as io:
    nwb = io.read()
    print(nwb)
