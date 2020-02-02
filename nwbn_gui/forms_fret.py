from nwbn_conversion_tools.gui.classes.forms_basic import BasicForm


class GroupFRET(BasicForm):
    def __init__(self, parent, metadata=None):
        """Groupbox for abc.FRET fields filling form."""
        super().__init__(title='FRET', parent=parent)
        #self.setTitle('FRET')
        self.parent = parent
        self.group_type = 'FRET'
        self.groups_list = []

        validator_float = QDoubleValidator()

        self.lbl_name = QLabel('name<span style="color:'+required_asterisk_color+';">*</span>:')
        self.lin_name = QLineEdit('FRET')
        self.lin_name.setToolTip("The name of this FRET.")

        self.lbl_description = QLabel('description:')
        if 'description' in metadata:
            self.lin_description = QLineEdit(metadata['description'])
        else:
            self.lin_description = QLineEdit('description')
        self.lin_description.setToolTip("Any notes or comments about the FRET")

        self.lbl_excitation_lambda = QLabel('excitation_lambda<span style="color:'+required_asterisk_color+';">*</span>:')
        if 'excitation_lambda' in metadata:
            self.lin_excitation_lambda = QLineEdit(str(metadata['excitation_lambda']))
        else:
            self.lin_excitation_lambda = QLineEdit('0.0')
        self.lin_excitation_lambda.setValidator(validator_float)

        self.lbl_donor = QLabel('donor:')
        self.donor_layout = QVBoxLayout()
        self.donor = QGroupBox()
        self.donor.setLayout(self.donor_layout)

        self.lbl_acceptor = QLabel('acceptor:')
        self.acceptor_layout = QVBoxLayout()
        self.acceptor = QGroupBox()
        self.acceptor.setLayout(self.acceptor_layout)

        self.grid = QGridLayout()
        self.grid.setColumnStretch(2, 1)
        self.grid.addWidget(self.lbl_name, 0, 0, 1, 2)
        self.grid.addWidget(self.lin_name, 0, 2, 1, 4)
        self.grid.addWidget(self.lbl_description, 1, 0, 1, 2)
        self.grid.addWidget(self.lin_description, 1, 2, 1, 4)
        self.grid.addWidget(self.lbl_excitation_lambda, 2, 0, 1, 2)
        self.grid.addWidget(self.lin_excitation_lambda, 2, 2, 1, 4)
        self.grid.addWidget(self.lbl_donor, 3, 0, 1, 2)
        self.grid.addWidget(self.donor, 3, 2, 1, 4)
        self.grid.addWidget(self.lbl_acceptor, 4, 0, 1, 2)
        self.grid.addWidget(self.acceptor, 4, 2, 1, 4)
        self.setLayout(self.grid)

    def refresh_objects_references(self, metadata=None):
        """Refreshes references with existing objects in parent group."""
        for child in self.groups_list:
            child.refresh_objects_references(metadata=metadata)

    def read_fields(self):
        """Reads fields and returns them structured in a dictionary."""
        data = {}
        data['name'] = self.lin_name.text()
        data['description'] = self.lin_description.text()
        data['excitation_lambda'] = float(self.lin_excitation_lambda.text())
        data['donor'] = self.donor_layout.itemAt(0).widget().read_fields()
        data['acceptor'] = self.acceptor_layout.itemAt(0).widget().read_fields()
        return data

    def write_fields(self, data={}):
        """Reads structured dictionary and write in form fields."""
        self.lin_name.setText(data['name'])
        self.lin_excitation_lambda.setText(str(data['excitation_lambda']))
        # Donor
        item = GroupFRETSeries(self, metadata=data['donor'])
        self.groups_list.append(item)
        self.donor_layout.addWidget(item)
        item.write_fields(data=data['donor'])
        # Acceptor
        item = GroupFRETSeries(self, metadata=data['acceptor'])
        self.groups_list.append(item)
        self.acceptor_layout.addWidget(item)
        item.write_fields(data=data['acceptor'])
        self.setContentLayout(self.grid)


class GroupFRETSeries(QGroupBox):
    def __init__(self, parent, metadata=None):
        """Groupbox for abc.FRETSeries fields filling form."""
        super().__init__(title='FRETSeries', parent=parent)
        self.setTitle('FRETSeries')
        self.parent = parent
        self.group_type = 'FRETSeries'

        validator_float = QDoubleValidator()

        self.lbl_name = QLabel('name<span style="color:'+required_asterisk_color+';">*</span>:')
        if 'name' in metadata:
            self.lin_name = QLineEdit(str(metadata['name']))
        else:
            self.lin_name = QLineEdit('FRETSeries')

        self.lbl_description = QLabel("description:")
        if 'description' in metadata:
            self.lin_description = QLineEdit(metadata['description'])
        else:
            self.lin_description = QLineEdit('description')

        self.lbl_device = QLabel('device<span style="color:'+required_asterisk_color+';">*</span>:')
        self.combo_device = CustomComboBox()
        self.combo_device.setToolTip("The device that was used to record")

        self.lbl_optical_channel = QLabel('optical_channel<span style="color:'+required_asterisk_color+';">*</span>:')
        self.optical_channel_layout = QVBoxLayout()
        self.optical_channel = QGroupBox()
        self.optical_channel.setLayout(self.optical_channel_layout)
        self.optical_channel.setToolTip(
            "One of possibly many groups storing channels pecific data")

        self.lbl_rate = QLabel("rate:")
        if 'rate' in metadata:
            self.lin_rate = QLineEdit(str(metadata['rate']))
        else:
            self.lin_rate = QLineEdit('0.0')
        self.lin_rate.setValidator(validator_float)

        self.lbl_fluorophore = QLabel("fluorophore:")
        if 'fluorophore' in metadata:
            self.lin_fluorophore = QLineEdit(str(metadata['fluorophore']))
        else:
            self.lin_fluorophore = QLineEdit('fluorophore')

        self.lbl_unit = QLabel('unit:')
        if 'unit' in metadata:
            self.lin_unit = QLineEdit(str(metadata['unit']))
        else:
            self.lin_unit = QLineEdit('')
        self.lin_unit.setPlaceholderText("unit")
        self.lin_unit.setToolTip("The base unit of measurement (should be SI unit)")

        self.grid = QGridLayout()
        self.grid.setColumnStretch(5, 1)
        self.grid.addWidget(self.lbl_name, 0, 0, 1, 2)
        self.grid.addWidget(self.lin_name, 0, 2, 1, 4)
        self.grid.addWidget(self.lbl_device, 1, 0, 1, 2)
        self.grid.addWidget(self.combo_device, 1, 2, 1, 4)
        self.grid.addWidget(self.lbl_optical_channel, 2, 0, 1, 2)
        self.grid.addWidget(self.optical_channel, 2, 2, 1, 4)
        self.grid.addWidget(self.lbl_rate, 3, 0, 1, 2)
        self.grid.addWidget(self.lin_rate, 3, 2, 1, 4)
        self.grid.addWidget(self.lbl_fluorophore, 4, 0, 1, 2)
        self.grid.addWidget(self.lin_fluorophore, 4, 2, 1, 4)
        self.grid.addWidget(self.lbl_unit, 5, 0, 1, 2)
        self.grid.addWidget(self.lin_unit, 5, 2, 1, 4)
        self.grid.addWidget(self.lbl_description, 6, 0, 1, 2)
        self.grid.addWidget(self.lin_description, 6, 2, 1, 4)
        self.setLayout(self.grid)

    def refresh_objects_references(self, metadata=None):
        """Refreshes references with existing objects in parent group."""
        self.combo_device.clear()
        for grp in self.parent.parent.groups_list:
            # Adds all existing Devices to combobox
            if isinstance(grp, GroupDevice):
                self.combo_device.addItem(grp.lin_name.text())

    def read_fields(self):
        """Reads fields and returns them structured in a dictionary."""
        data = {}
        data['name'] = self.lin_name.text()
        data['description'] = self.lin_description.text()
        data['device'] = str(self.combo_device.currentText())
        data['optical_channel'] = []
        nItems = self.optical_channel_layout.count()
        for i in range(nItems):
            item = self.optical_channel_layout.itemAt(i).widget()
            data['optical_channel'].append(item.read_fields())
        data['rate'] = float(self.lin_rate.text())
        data['fluorophore'] = self.lin_fluorophore.text()
        data['unit'] = self.lin_unit.text()
        return data

    def write_fields(self, data={}):
        """Reads structured dictionary and write in form fields."""
        self.lin_name.setText(data['name'])
        self.lin_description.setText(data['description'])
        self.combo_device.clear()
        self.combo_device.addItem(data['device'])
        nItems = self.optical_channel_layout.count()
        for ind, sps in enumerate(data['optical_channel']):
            if ind >= nItems:
                item = GroupOpticalChannel(self, metadata=data['optical_channel'][ind])
                self.optical_channel_layout.addWidget(item)
        self.lin_fluorophore.setText(data['fluorophore'])
        self.lin_unit.setText(data['unit'])
