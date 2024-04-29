from . import models


def create_data():
    name_t = ("John Doe", "Jane Doe", "John Smith", "Jane Smith")

    modellist = []
    for name in name_t:
        modellist.append(models.SimpleModel(name=name, description="friend"))
    models.SimpleModel.objects.bulk_create(modellist)
