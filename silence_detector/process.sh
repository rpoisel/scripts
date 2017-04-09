#!/bin/bash

INPUT_DIR=$1
OUTPUT_DIR=$2

rm -rf  "${OUTPUT_DIR}"
mkdir -p "${OUTPUT_DIR}"

SCRIPT_DIR="`dirname \"$0\"`"
SCRIPT_DIR="`( cd \"$SCRIPT_DIR\" && pwd )`"
if [ -z "${SCRIPT_DIR}"]
then
  # error; for some reason, the path is not accessible
  # to the script (e.g. permissions re-evaled after suid)
  exit 1
fi

while IFS= read -d '' -u 5 -r original
do
    TMPFILE="$(mktemp --dry-run)"
    IN_FILE="${INPUT_DIR}/${original}"
    OUT_FILE="${OUTPUT_DIR}/${original/.m4a/.wav}"
    echo "${IN_FILE} => ${TMPFILE} => ${OUT_FILE}"
    (cd "${INPUT_DIR}" \
        && ffmpeg <&1- -i "${IN_FILE}" -y -f wav -acodec pcm_s16le -ac 2 "${TMPFILE}" \
    )
    python3 ${SCRIPT_DIR}/silence_detector.py "${TMPFILE}" "${OUT_FILE}"
    test -e "${TMPFILE}" && rm "${TMPFILE}"
done 5< <(cd "${INPUT_DIR}" && find . -type f -name '*.m4a' -print0)
