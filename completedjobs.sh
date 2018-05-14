#!/bin/bash

sacct -u yar2 \
    -X \
    -P \
    --format JobID,JobName,Submit,State
