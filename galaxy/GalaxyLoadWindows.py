__author__ = 'AleB'

from pandas import Series

from ParamExecClass import ParamExecClass
from pyHRV.windowing import NamedWinGen, CollectionWinGen, Window


class GalaxyLoadWindows(ParamExecClass):
    """
    kwargs['input'] ----> input file
    kwargs['output'] ---> output file
    kwargs['format'] ---> one in [ 'excel', 'csv' ]
                 default: 'csv'
    kwargs['column'] ---> column to load
                 default: PyHRVSettings.load_rr_column_name
    kwargs['sheet'] ---> excel's sheet's name or ordinal number
                 default: None if format != 'excel'
    kwargs['windows_type'] ---> windows type in [ 'labeled_sequences', 'begin_values' ]
    """

    def execute(self):
        output_file = self._kwargs['output']
        c = self.load_column()

        if self._kwargs['windows_type'] == 'labeled_sequences':
            w = NamedWinGen(None, c)
        else:
            if self._kwargs['windows_type'] == 'begin_values':
                w = map(self.__class__.map_end_window, c)[1:]
                w = CollectionWinGen(None, w)
            else:
                raise NotImplemented("Not implemented windowing mode: %s" % self._kwargs['windows_type'])
        Series(w).save(output_file)

    def map_end_window(self, end):
        if self.__s is None:
            self.__s = end
        else:
            return Window(self.__s, end)