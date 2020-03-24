from traits.api import Instance

from force_bdss.api import BaseDataSource, DataValue, Slot

from force_chemtools.io.base_file_reader import BaseFileReader

class MissingFragmentException(Exception):
    pass


class FragmentDataSource(BaseDataSource):
    """Class takes in all data required to define each
    separate molecular fragment in a Gromacs experiment. Gromacs topology
    files must be included for all species, however coordinate files
    are not necessary for atoms or molecules represented by single beads. BLAS VBLA
    """

    _reader = Instance(BaseFileReader)

    def run(self, model, parameters):
        """Simply wraps all user input in a `GromacsFragment` object for further
        processing. Consequently, it is expected that either this method
        can be overloaded by a subclass to perform more specific actions,
        of additional `DataSource` objects can perform this in the next
        `ExecutionLayer`"""

        # Obtain all fragments present in topology file
        fragments = self._reader.read(model.topology)

        # Search for fragment with symbol referenced in model
        indices = [
            index for index, fragment in enumerate(fragments)
            if fragment.symbol == model.symbol
        ]
        try:
            fragment = fragments[indices[0]]
        except IndexError as e:
            raise MissingFragmentException(
                f'Fragment with symbol {model.symbol} has not'
                f'been found in Gromacs topology file {model.topology}'
            ) from e

        # Assign a human readable name and Gromacs coordinate file
        # to the fragment that are contributed by model
        fragment.name = model.name
        fragment.coordinate = model.coordinate

        return [DataValue(type="FRAGMENT", value=fragment)]

    def slots(self, model):
        return (
            (
            ),
            (
                Slot(type="FRAGMENT",
                     description="Gromacs GromacsFragment data object"),
            )
        )