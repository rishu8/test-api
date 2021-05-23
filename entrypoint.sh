#!/usr/bin/env bash

set -o errexit
set -o pipefail

#cmd=`echo "python $@" | envsubst`
cmd=`echo "$@" | envsubst`
echo "--- Command ---------------------------------"
echo "${cmd}"
echo "---------------------------------------------"

exec ${cmd[@]}
