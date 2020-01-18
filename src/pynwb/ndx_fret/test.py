from pynwb import NWBFile, NWBHDF5IO, ProcessingModule
from pynwb.device import Device
from pynwb.ophys import OpticalChannel
from pynwb.image import ImageSeries
from ndx_fret import FRET, FRETSeries

from datetime import datetime
import numpy as np

nwb = NWBFile('session_description', 'identifier', datetime.now().astimezone())

# Create and add device
device = Device(name='Device')
nwb.add_device(device)

# Ophys processing module
ophys_module = ProcessingModule(
    name='Ophys',
    description='contains optical physiology processed data.',
)
nwb.add_processing_module(ophys_module)

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

# Create FRET
data_donor = ImageSeries(
    name='ImageSeries_donor',
    description='',
    data=np.random.randn(100, 10, 10),
    rate=60.,
    unit='',
)
fs_d = FRETSeries(
    name='FRETSeries_donor',
    fluorophore='mCitrine',
    optical_channel=opt_ch_d,
    device=device,
    data=data_donor,
    emission_lambda=0.0
)

data_acceptor = ImageSeries(
    name='ImageSeries_acceptor',
    description='',
    data=np.random.randn(100, 10, 10),
    rate=60.,
    unit='',
)
fs_a = FRETSeries(
    name='FRETSeries_acceptor',
    fluorophore='mKate2',
    optical_channel=opt_ch_a,
    device=device,
    data=data_acceptor,
    emission_lambda=0.0
)

fret = FRET(
    name='FRET',
    excitation_lambda=482.,
    donor=fs_d,
    acceptor=fs_a
)
nwb.add_acquisition(fret)
print(nwb)

# Write nwb file
with NWBHDF5IO('test_fret.nwb', 'w') as io:
    io.write(nwb)
    print('NWB file written')

# Read nwb file and check its content
with NWBHDF5IO('test_fret.nwb', 'r', load_namespaces=True) as io:
    nwb = io.read()
    print(nwb)
