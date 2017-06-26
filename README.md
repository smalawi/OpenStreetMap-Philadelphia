# OpenStreetMap-wrangling

## Files included

* **data.py**: cleans .osm file and converts to .csv files
* **cleaning.py**: contains scripts for cleaning specific tags on OSM data
* **database.py**: used to query database (after tables are generated from .csv files)
* **schema.py**: schema for conversion of .osm to .csv files used in data.py
* **sampler.py**: takes a fraction of the top-level tags from an .osm file to build a smaller sample


* **sample2.osm**: sample of Philadelphia OSM data, generated using sampler.py
* **resources.md**: list of outside resources consulted during the completion of this project

* **osm-wrangling.pdf/md**: final report in pdf and markdown formats. [View as gist here](https://gist.github.com/smalawi/a48b161b67751b83afb7693a94166398)

## Usage

Generate .csv files:
```
python data.py
```

Import into database via command line (sqlite3).

Query database:
```
python database.py
```