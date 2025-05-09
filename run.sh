#!/bin/bash

find examples/. -mindepth 1 -type d -exec ./vue_to_md.py {} \;

