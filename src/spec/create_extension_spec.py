from pynwb.spec import NWBNamespaceBuilder, NWBGroupSpec
from export_spec import export_spec

def main():
    ns_builder = NWBNamespaceBuilder(doc='type for storing time-varying FRET data',
                                     name='ndx-fretseries',
                                     version='0.0.1',
                                     author='Luiz Tauffer and Ben Dichter',
                                     contact='ben.dichter@gmail.com')

    ns_builder.include_type('NWBDataInterface', namespace='core')
    ns_builder.include_type('OpticalChannel', namespace='core')

    FRETSeries = NWBGroupSpec(
        doc='type for storing time-varying FRET data',
        neurodata_type_def='FRETSeries',
        neurodata_type_inc='NWBDataInterface',
        )

    FRETSeries.add_attribute(
        name='excitation_lambda',
        doc='Excitation wavelength in nm.',
        dtype='float',
        shape=None,
    )
    FRETSeries.add_attribute(
        name='fluorophore_donor',
        doc='Fluorophore of donor',
        dtype='text',
        shape=None,
    )
    FRETSeries.add_attribute(
        name='fluorophore_acceptor',
        doc='Fluorophore of acceptor',
        dtype='text',
        shape=None,
    )
    FRETSeries.add_attribute(
        name='Location',
        doc='Location of imaging field.',
        dtype='text',
        shape=None,
        required=False,
    )
    FRETSeries.add_attribute(
        name='Unit',
        doc='The base unit of measurement (should be SI unit).',
        dtype='text',
        shape=None,
        required=False,
    )
    FRETSeries.add_attribute(
        name='Conversion',
        doc='Scalar to multiply each element in data to convert it to the specified unit.',
        dtype='float',
        shape=None,
        required=False,
    )

    FRETSeries.add_dataset(
        name='data_donor',
        doc='Fluorescence data from donor.',
        dims=(('time',), ('time', 'x'), ('time', 'x', 'y')),
        shape=((None,), (None, None), (None, None, None)),
        dtype='float',
    )
    FRETSeries.add_dataset(
        name='data_acceptor',
        doc='Fluorescence data from acceptor.',
        dims=(('time',), ('time', 'x'), ('time', 'x', 'y')),
        shape=((None,), (None, None), (None, None, None)),
        dtype='float',
    )

    FRETSeries.add_attribute(
        name='rate',
        doc='Rate images are acquired, in Hz.',
        dtype='float',
        shape=None,
    )
    FRETSeries.add_attribute(
        name='starting_time',
        doc='The timestamp of the first sample.',
        dtype='float',
        shape=None,
        required=False
    )
    FRETSeries.add_dataset(
        name='timestamps',
        doc='Timestamps for samples stored in data.',
        dims=('timestamps',),
        shape=(None,),
        dtype='float',
        quantity='?'
    )

    FRETSeries.add_group(
        name='optical_channel_donor',
        doc='Group storing channel specific data',
        neurodata_type_inc='OpticalChannel',
        quantity='?'
    )
    FRETSeries.add_group(
        name='optical_channel_acceptor',
        doc='Group storing channel specific data',
        neurodata_type_inc='OpticalChannel',
        quantity='?'
    )
    FRETSeries.add_link(
        name='device',
        doc='The device that was used to record.',
        target_type='Device',
    )

    new_data_types = [FRETSeries]

    export_spec(ns_builder, new_data_types)


if __name__ == "__main__":
    main()
