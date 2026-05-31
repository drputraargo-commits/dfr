#!/bin/bash
lscpu
BATCH_SIZE=1
INPUT_DIM=10

python trace_model.py \
    --batch-size ${BATCH_SIZE} \
    --input-dim ${INPUT_DIM}
