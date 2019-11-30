#!/bin/bash
set -e

exec bash -c -l "cd /app && $*"
