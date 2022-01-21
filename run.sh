#!/bin/bash
PYTHON="$PWD/venv/bin/python"
SCRIPT="$PWD/parser.py"

TEMPLATE=$1
OUTPUT=$2

if [ -z "$TEMPLATE" ] || [ -z "$OUTPUT" ]; then
    echo "Usage: run.sh <template> <output>"
    exit 1
fi

if [ ! -f "$PYTHON" ]; then
    echo "Python not found: $PYTHON"
    exit 1
fi

if [ ! -f "$SCRIPT" ]; then
    echo "Script not found: $SCRIPT"
    exit 1
fi

if [ ! -f "$TEMPLATE" ]; then
    echo "Template not found: $TEMPLATE"
    exit 1
fi

HEAD="-H"
for CONFIG in $(ls $PWD/configs/*.cfg)
do
    echo -n "Parse $(basename $CONFIG) ... "
    $PYTHON $SCRIPT $HEAD $TEMPLATE $CONFIG >> $OUTPUT 2>/dev/null && echo "Ok" || echo "Fail"

    if [ $? -eq 0 ]; then HEAD=""; fi
done
