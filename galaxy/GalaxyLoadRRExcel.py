__author__ = 'AleB'

from ParamExecClass import ParamExecClass
from pyHRV.Files import save_data_series, load_excel_column


class GalaxyLoadRR(ParamExecClass):
    """
    ONLY RR..
    kwargs['input'] ----> input file
    kwargs['output'] ---> output file
    kwargs['column'] ---> column to load
                 default: PyHRVSettings.load_rr_column_name
    kwargs['sheet'] ---> excel's sheet's name or ordinal number
    """

    def execute(self):
        out = self._kwargs['output']

        save_data_series(self.load_column(), out)

    def load_column(self):
        return load_excel_column(self._kwargs['input'], self._kwargs['column'], None, self._kwargs['sheet'])