from pynwb.spec import NWBNamespaceBuilder, NWBGroupSpec
from export_spec import export_spec

def main():
    ns_builder = NWBNamespaceBuilder(doc='type for storing time-varying FRET data',
                                     name='ndx-fretseries',
                                     version='0.0.1',
                                     author='Luiz Tauffer and Ben Dichter',
                                     contact='ben.dichter@gmail.com')

    FRETSeries = NWBGroupSpec(
        doc='type for storing time-varying FRET data',
        neurodata_type_def='FRETSeries',
        neurodata_type_inc='TimeSeries',
        )

    new_data_types = [FRETSeries]

    ns_builder.include_type('TimeSeries', namespace='core')

    export_spec(ns_builder, new_data_types)


if __name__ == "__main__":
    main()
