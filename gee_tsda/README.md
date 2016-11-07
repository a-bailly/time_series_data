# GEE-TSDA dataset

## Experiments of domain adaptation problems ##

Target domain is aligned with Source domain.
RD-2, SSMA and KEMA use labeled information from both domains.
RD-1 uses only labeled information from target domain.
RD-1 and RD-2 correspond to classification on Raw Data with a linear discriminant analysis classifier (L-DAC).
SSMA and KEMA project the time series in a common latent before classifying with the L-DAC.
Best accuracy for each domain is provided in bold.

| Target | RD-1 | RD-2 | SSMA | KEMA |
| :----: | :----: | :----: | :----: | :----: |
| A | 0.542 | 0.263 | 0.636 | **0.724** |
| B | 0.554 | 0.411 | 0.627 | **0.631** |
| C | 0.293 | 0.281 | 0.376 | **0.532** |
| D | 0.188 | 0.169 | 0.265 | **0.412** |
| E | 0.515 | 0.074 | 0.385 | **0.534** |

## File Format ##

Each line corresponds to a labeled time series.

Fisrt column is the label, the following numbers are the different time instant of the time series.

`L t_1 t_2 t_3 ... t_n`

## File Description ##

### Description

| Name | Ref | \# of Time Series | Length | Satellite | Temporal Resolution | Geographical Area | Year | Vegetation Index | ImageCollection ID |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| modis_eu_ndvi_8day_2011.txt | Source | 311 | 46 | MODIS | 8 days | Europe | 2011 | NDVI | `MODIS/MCD43A4_NDVI` |
| modis_sa_ndvi_8day_2011.txt | A |  338 | 46 | MODIS | 8 days | South America | 2011 | NDVI | `MODIS/MCD43A4_NDVI` |
| modis_na_ndvi_8day_2011.txt | B | 344 | 46 | MODIS | 8 days | North America | 2011 | NDVI | `MODIS/MCD43A4_NDVI` |
| modis_eu_ndvi_8day_2003.txt | C | 389 | 46 | MODIS | 8 days | Europe | 2003 | NDVI | `MODIS/MCD43A4_NDVI` |
| landsat_eu_ndvi_8day_2011.txt | D | 355 | 41 | LANDSAT | 8 days | Europe | 2011 | NDVI | `LANDSAT/LT5_L1T_8DAY_NDVI` |
| modis_eu_lai_4day_2011.txt | E | 339 | 91 | MODIS | 4 days | Europe | 2011 | LAI | `MODIS/006/MCD15A3H` |

### List of class

* Evergreen Forest
* Deciduous Forest
* Shrublands
* Savannas
* Grasslands
* Croplands

### Summary of the number of time series per class

| Ref | Total | Evergreen Forest | Deciduous Forest | Shrublands | Savannas | Grasslands | Croplands |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| Source | 311 | 11 | 27 | 20 | 47 | 14 | 192 |
| A |  338 | 48 | 60 | 58 | 94 | 46 | 32 |
| B | 344 | 12 | 31 | 66 | 36 | 121 | 78 |
| C | 389 | 16 | 29 | 33 | 42 | 27 | 242 |
| D | 355 | 11 | 32 | 21 | 51 | 14 | 226 |
| E | 339 | 9  | 31 | 21 | 58 | 19 | 201 |

### Mean profil per class per domain

| Ref | Preview |
| :----: | :----: |
| Source | ![Source Mean Profil](https://github.com/a-bailly/time_series_data/blob/master/gee_tsda/img/Source_profil.png) |
| A | ![A Mean Profil](https://github.com/a-bailly/time_series_data/blob/master/gee_tsda/img/A_profil.png) |
| B | ![B Mean Profil](https://github.com/a-bailly/time_series_data/blob/master/gee_tsda/img/B_profil.png) |
| C | ![C Mean Profil](https://github.com/a-bailly/time_series_data/blob/master/gee_tsda/img/C_profil.png) |
| D | ![D Mean Profil](https://github.com/a-bailly/time_series_data/blob/master/gee_tsda/img/D_profil.png) |
| E | ![E Mean Profil](https://github.com/a-bailly/time_series_data/blob/master/gee_tsda/img/E_profil.png) |

### Extraction Map

![GEE-TSDA Extraction Map](https://github.com/a-bailly/time_series_data/blob/master/gee_tsda/img/gee_extraction_map.png)

Each black polygon correspond to the area where time series are extracted.
Coordinates are available in the file *gee_time_series_extraction.gee*.

## Code for time series extraction ##

The file *gee_time_series_extraction.gee* contains the code that extracts the time series from the [Google Earth Engine](https://code.earthengine.google.com/) Framework.

