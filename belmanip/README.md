# BELMANIP dataset

## File Format ##

Each line corresponds to a labeled time series.

Fisrt column is the label, the following numbers are the different time instant of the time series.

`L t_1 t_2 t_3 ... t_n`

## File Description ##

### Description

| Name | Ref | \# of Time Series | Length | Satellite | Temporal Resolution | Geographical Area | Year | Vegetation Index |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| fapar.txt | fAPAR | 86 | 36 | SPOT | 10 days | North America | 2012 | fAPAR |
| fvc.txt | FVC | 86 | 36 | SPOT | 10 days | North America | 2012 | FVC |

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
| Per Modality | 86 | 14 | 4 | 12 | 3 | 16 | 19 |

### Map

![Image BELMANIP Map](https://github.com/a-bailly/time_series_data/blob/master/belmanip/img/belmanip_map.png)

Label information provided by [BELMANIP](http://calvalportal.ceos.org/web/olive/site-description) are taken from all over the world.
We here focus on the darker area shown on the map, which roughly correspond to North America.
This area was chosen as it features the highest class diversity into a limited space.
