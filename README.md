### A Longitudinal View of Netflix: Content Delivery over IPv6 and Content Cache Deployments

Trinh Viet Doan (Technical University of Munich) | Vaibhav Bajpai (Technical University of Munich) | Sam Crawford (SamKnows)


[IEEE INFOCOM 2020](https://infocom2020.ieee-infocom.org/), July 6&ndash;9, 2020. [Pre-print available &rarr;](http://home.in.tum.de/~doan/2020-netflix-delivery.pdf) 

---

### Vantage Points

The dataset is collected from ~100 SamKnows probes:

![](http://i.imgur.com/zVefNfd.png)


### Dataset

The raw datasets are available at:

* [Technical University of Munich, mediaTUM &rarr; TBD]  [](http://doi.org/...)

The data consists of two sqlite3 databases, one for the measurements by the `netflix` test (`netflix-data.db`), the other one for the throughput measurements toward MLab (`mlab-data.db`).  

The schemas of the tables can be found under [`./data/netflix-schema.sql`](https://github.com/tv-doan/infocom-2020-netflix/blob/master/data/netflix-schema.sql)) and [`./data/mlab-schema.sql`](https://github.com/tv-doan/infocom-2020-netflix/blob/master/data/mlab-schema.sql)).

This repository contains (most of) the required code and metadata to reproduce the results, see below for further instructions.

### Requirements

To read from the database (see above), `sqlite3` is needed.
The analyses were performed using `jupyter` notebooks on `Python 2.7`.
Required Python dependencies are listed in [`requirements.txt`](https://github.com/tv-doan/infocom-2020-netflix/blob/master/requirements.txt) and can be installed using `pip install -r requirements.txt`.

For the calculation of CDFs and drawing of the corresponding plots, [`Pmf.py` &rarr;](http://greenteapress.com/thinkstats/Pmf.py) and [`Cdf.py` &rarr;](http://greenteapress.com/thinkstats/Cdf.py) from [Think Stats &rarr;](https://greenteapress.com/wp/think-stats-2e/) are used.

### Repeating the results
Move the required datasets and modules to the right locations:
- `netflix-data.db` &rarr; [`./data/`](https://github.com/tv-doan/infocom-2020-netflix/tree/master/data)
- `mlab-data.db` &rarr; [`./data/`](https://github.com/tv-doan/infocom-2020-netflix/tree/master/data)
- `Pmf.py` &rarr; [`./notebooks/`](https://github.com/tv-doan/infocom-2020-netflix/tree/master/notebooks)
- `Cdf.py` &rarr; [`./notebooks/`](https://github.com/tv-doan/infocom-2020-netflix/tree/master/notebooks)

Run the [`aggregation.ipynb`](https://github.com/tv-doan/infocom-2020-netflix/blob/master/notebooks/aggregation.ipynb) notebook to process and aggregate the raw dataset, which will store the results in a separate database. After that, the other notebooks `fig-*.ipynb` can be used to draw the plots presented in the paper.
All plots are saved under [`./plots/`](https://github.com/tv-doan/infocom-2020-netflix/tree/master/plots).

Note: the lookup of metadata was already done, however, it can be repeated by running [`./metadata/netflix-metadata-lookup.py`](https://github.com/tv-doan/infocom-2020-netflix/blob/master/metadata/netflix-metadata-lookup.py) and [`./metadata/probe-to-timezone.ipynb`](https://github.com/tv-doan/infocom-2020-netflix/blob/master/metadata/probe-to-timezone.ipynb).


### Contact

Please feel welcome to contact the authors for further details.

- Trinh Viet Doan (<doan@in.tum.de>) (corresponding author)
- Vaibhav Bajpai (<bajpaiv@in.tum.de>)
- Sam Crawford (<sam@samknows.com>)
