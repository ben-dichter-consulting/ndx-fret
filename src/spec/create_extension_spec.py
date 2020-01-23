from pynwb.spec import NWBNamespaceBuilder, NWBGroupSpec, NWBAttributeSpec, NWBLinkSpec, NWBDatasetSpec, export_spec
import os

def main():
    ns_builder = NWBNamespaceBuilder(doc='type for storing time-varying FRET data',
                                     name='ndx-fret',
                                     version='0.1.0',
                                     author='Luiz Tauffer and Ben Dichter',
                                     contact='ben.dichter@gmail.com')

    ns_builder.include_type('NWBDataInterface', namespace='core')
    ns_builder.include_type('NWBContainer', namespace='core')
    ns_builder.include_type('ImageSeries', namespace='core')
    ns_builder.include_type('OpticalChannel', namespace='core')

    # Define FRETSeries, type that stores Donor/Acceptor specific information
    FRETSeries = NWBGroupSpec(
        neurodata_type_def='FRETSeries',
        neurodata_type_inc='ImageSeries',
        doc='Donor/Acceptor specific information.',
    )

    FRETSeries.add_attribute(
        name='fluorophore',
        doc='Fluorophore name.',
        dtype='text',
        shape=None,
    )
    FRETSeries.add_attribute(
        name='emission_lambda',
        doc='Emission wavelength (in nm).',
        dtype='float',
        shape=None,
    )
    FRETSeries.add_group(
        name='optical_channel',
        doc='Group storing channel specific data',
        neurodata_type_inc='OpticalChannel',
    )
    FRETSeries.add_link(
        name='device',
        doc='The device that was used to record.',
        target_type='Device',
    )

    # Defines FRET, DataInterface that holds metadata and data for FRET experiments
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
        name='location',
        doc='Location of imaging field.',
        dtype='text',
        shape=None,
        required=False,
    )
    FRET.add_group(
        name='donor',
        doc='Group storing donor data',
        neurodata_type_inc='FRETSeries',
    )
    FRET.add_group(
        name='acceptor',
        doc='Group storing acceptor data',
        neurodata_type_inc='FRETSeries',
    )

    new_data_types = [FRET, FRETSeries]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    main()
