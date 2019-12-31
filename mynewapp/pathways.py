from opal.core.pathway import PagePathway
from mynewapp import models


class AddPatient(PagePathway):
    display_name = "Add Patient"
    slug = "add_patient"
    icon = 'fa-plus'

    steps = [
        models.Demographics
    ]