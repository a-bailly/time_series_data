# GEE-TSDA dataset

## File Format ##

Each line corresponds to a labeled time series.

Fisrt column is the label, the following numbers are the different time instant of the time series.

`L t_1 t_2 t_3 ... t_n`

## File Description ##

### Description

| Name | Ref | \# of Time Series | Length | Satellite | Temporal Resolution | Geographical Area | Year | Vegetation Index | ImageCollection ID |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| modis_eu_ndvi_8day_2011.txt | Source | 49517 | 46 | MODIS | 8 days | Europe | 2011 | NDVI | `MODIS/MCD43A4_NDVI` |
| modis_sa_ndvi_8day_2011.txt | A | 45811 | 46 | MODIS | 8 days | South America | 2011 | NDVI | `MODIS/MCD43A4_NDVI` |
| modis_na_ndvi_8day_2011.txt | B | 38367 | 46 | MODIS | 8 days | North America | 2011 | NDVI | `MODIS/MCD43A4_NDVI` |
| modis_eu_ndvi_8day_2003.txt | C | 52824 | 46 | MODIS | 8 days | Europe | 2003 | NDVI | `MODIS/MCD43A4_NDVI` |
| landsat_eu_ndvi_8day_2011.txt | D | 36820 | 41 | LANDSAT | 8 days | Europe | 2011 | NDVI | `LANDSAT/LT5_L1T_8DAY_NDVI` |
| modis_eu_lai_4day_2011.txt | E | 20206 | 91 | MODIS | 4 days | Europe | 2011 | LAI | `MODIS/006/MCD15A3H` |

### List of class

* Evergreen Forest
* Deciduous Forest
* Shrublands
* Savannas
* Grasslands
* Croplands

### Summary of the number of time series per class

| Ref | Total | Evergreen Forest | Deciduous Forest | Shrublands | Savannas | Grasslands | Croplands |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| Source | 49517 |  3% |  9% |  5% | 15% |  6% | 61% |
| A      | 45811 | 10% | 22% | 15% | 34% | 12% |  7% |
| B      | 38367 |  4% |  8% | 22% |  9% | 38% | 19% |
| C      | 52824 |  3% |  8% |  9% | 13% |  8% | 59% |
| D      | 36820 |  3% |  9% |  5% | 15% |  6% | 61% |
| E      | 20206 |  3% | 10% |  5% | 15% |  6% | 61% |

### Mean profil per class per domain

| Ref | Preview |
| :----: | :----: |
| Source | ![Source Mean Profil](https://github.com/a-bailly/time_series_data/blob/master/dl_tsda/img/source.png) |
| A | ![A Mean Profil](https://github.com/a-bailly/time_series_data/blob/master/dl_tsda/img/sa.png) |
| B | ![B Mean Profil](https://github.com/a-bailly/time_series_data/blob/master/dl_tsda/img/na.png) |
| C | ![C Mean Profil](https://github.com/a-bailly/time_series_data/blob/master/dl_tsda/img/2003.png) |
| D | ![D Mean Profil](https://github.com/a-bailly/time_series_data/blob/master/dl_tsda/img/landsat.png) |
| E | ![E Mean Profil](https://github.com/a-bailly/time_series_data/blob/master/dl_tsda/img/lai.png) |

### Extraction Map

![GEE-TSDA Extraction Map](https://github.com/a-bailly/time_series_data/blob/master/gee_tsda/img/gee_extraction_map.png)

Each black polygon correspond to the area where time series are extracted.
Coordinates are available in the file *gee_time_series_extraction.gee*.

## Citations

If you use the GEE-TSDA dataset in a scientific publication, we would appreciate citations:

```
@misc{gee-tsda,
  title  = {{Google Earth Engine - Time Series Domain Adaptation Dataset}},
  author = {{Bailly, Adeline}},
  year   = {2017},
  note   = {\url{github.com/a-bailly/time_series_data/dl_tsda}}
}
```

## License

Under [GNU General Public License](https://www.gnu.org/licenses/gpl-3.0.en.html)

