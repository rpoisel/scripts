#!/bin/bash

if [ $# -ne 2 ]
then
  echo "Usage: $0 <base-dir> <output-base>"
  exit 1
fi

INPUT_DIR=$1
OUTPUT_DIR=$2

while IFS= read -d $'\0' -u 5 -r file
do
  # using exiv2 to retrieve EXIF data from jpegs
  TARGET_SUBDIR=$(exiv2 -K Exif.Photo.DateTimeOriginal -pt ${file} 2>/dev/null | awk '{print $4}' | sed 's/:/\//g')
  if [ -z ${TARGET_SUBDIR+x} ] || [ -z "${TARGET_SUBDIR}" ]
  then
    TARGET_SUBDIR=unclassified
  fi
  echo "${file} => '${TARGET_SUBDIR}'"
  if [ ! -e ${OUTPUT_DIR}/${TARGET_SUBDIR} ]
  then
    mkdir -p ${OUTPUT_DIR}/${TARGET_SUBDIR}
  fi
  mv ${file} ${OUTPUT_DIR}/${TARGET_SUBDIR}
done 5< <(find ${INPUT_DIR} -type f -name '*.jpg' -size +1M -print0 2>/dev/null)

