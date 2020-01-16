from pynwb.spec import NWBNamespaceBuilder, NWBGroupSpec, export_spec
import os

def main():
    ns_builder = NWBNamespaceBuilder(doc='type for storing time-varying FRET data',
                                     name='ndx-fret',
                                     version='0.0.1',
                                     author='Luiz Tauffer and Ben Dichter',
                                     contact='ben.dichter@gmail.com')

    ns_builder.include_type('NWBDataInterface', namespace='core')
    ns_builder.include_type('ImageSeries', namespace='core')
    ns_builder.include_type('OpticalChannel', namespace='core')

    FRET = NWBGroupSpec(
        doc='type for storing time-varying FRET data',
        neurodata_type_def='FRET',
        neurodata_type_inc='NWBDataInterface',
    )

    FRET.add_attribute(
        name='excitation_lambda',
        doc='Excitation wavelength in nm.',
        dtype='float',
        shape=None,
    )
    FRET.add_attribute(
        name='fluorophore_donor',
        doc='Fluorophore of donor',
        dtype='text',
        shape=None,
    )
    FRET.add_attribute(
        name='fluorophore_acceptor',
        doc='Fluorophore of acceptor',
        dtype='text',
        shape=None,
    )
    FRET.add_attribute(
        name='location',
        doc='Location of imaging field.',
        dtype='text',
        shape=None,
        required=False,
    )

    FRET.add_group(
        name='data_donor',
        doc='Fluorescence data from donor.',
        neurodata_type_inc='ImageSeries',
        quantity=1
    )
    FRET.add_group(
        name='data_acceptor',
        doc='Fluorescence data from acceptor.',
        neurodata_type_inc='ImageSeries',
        quantity=1
    )

    FRET.add_group(
        name='optical_channel_donor',
        doc='Group storing channel specific data',
        neurodata_type_inc='OpticalChannel',
        quantity='?'
    )
    FRET.add_group(
        name='optical_channel_acceptor',
        doc='Group storing channel specific data',
        neurodata_type_inc='OpticalChannel',
        quantity='?'
    )

    FRET.add_link(
        name='device',
        doc='The device that was used to record.',
        target_type='Device',
    )


    new_data_types = [FRET]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    main()
