# Import local modules
from photoshop_python_api._core import Core
from photoshop_python_api._basic_option import BasicOption


class TiffSaveOptions(BasicOption, Core):
    object_name = 'TiffSaveOptions'

    def __int__(self):
        super(TiffSaveOptions, self).__init__()
