# Compumedics Reader

cpmreader is a package to read raw compumedics polysomnography files

## Installation

Run the following command to install cpmreader

```bash
pip install git+https://github.com/bastienlechat/Compumedics-reader.git
```

## Usage

We have a high level function to import raw data, hypnogram and event scoring.

```python
from cpmreader.cpm import read_psg_compumedics
folder = "path/to/your/compumedics/folder"
raw,hypnogram,events = read_psg_compumedics(folder=folder,
                                            mne_output=False)
```

This will read all available raw data into memory, if you just want to 
include a subset of channel for faster loading, use the "include" parameter, 
e.g, :

```python
from cpmreader.cpm import read_psg_compumedics, cpm_what_channels
folder = "path/to/your/compumedics/folder"

#read montage and return a list of channel
available_channels = cpm_what_channels(folder)

#only load EEG channel C3 C4 and ref channels
raw,hypnogram,events = read_psg_compumedics(folder=folder,
                                            include=['C3','C4','M1','M2']
                                            mne_output=False)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.