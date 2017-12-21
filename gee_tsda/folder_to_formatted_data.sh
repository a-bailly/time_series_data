#!/usr/bin/env bash

rm *~ */x*.txt

#folder='2011_SouthAm_MODIS_NDVI/'
#output='modis_sa_ndvi_8day_2011.txt'

#folder='2011_NorthAm_MODIS_NDVI/'
#output='modis_na_ndvi_8day_2011.txt'

#folder='2011_Eu_MODIS_NDVI/'
#output='modis_eu_ndvi_8day_2011.txt'

#folder='2011_Eu_LANDSAT_NDVI/'
#output='landsat_eu_ndvi_8day_2011.txt'

folder='2011_EU_MODIS_LAI/'
output='modis_eu_lai_4day_2011.txt'

cat 'gee_tsda/'$output > $output

mv $folder'ee-chart.csv' $folder'ee-chart(0).csv'

count=$(ls *$folder | wc -l)
echo 'nb_files: '$count

cp=0
for ((x=0;x<count;x=x+2)); do
	arg1='gee_to_tsc.py'
	arg2=$folder'ee-chart('$((x+1))').csv'
	arg3=$folder'ee-chart('$x').csv'
	arg4=$folder'x'$cp'.txt'
	size1=`wc -l "$arg2" | cut -d ' ' -f1`
	size2=`wc -l "$arg3" | cut -d ' ' -f1`
	while ((size1 != 4 || size2 < 5)) && (($x < $count))
	do
		x=$((x+1))
		if (($((x+1)) < $count))
		then
			arg2=$folder'ee-chart('$((x+1))').csv'
			arg3=$folder'ee-chart('$x').csv'
			size1=`wc -l "$arg2" | cut -d ' ' -f1`
			size2=`wc -l "$arg3" | cut -d ' ' -f1`
		fi
	done
	python $arg1 $arg2 $arg3 $arg4
	cat $folder'x'$cp'.txt' >> $output
	cp=$((cp+1))
done
