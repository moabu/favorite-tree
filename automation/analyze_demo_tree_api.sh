#!/bin/bash
set -euo pipefail

collect_logs() {
 # Place holder function that would collect logs if failed and send them possibly to IM or as a PR comment
 echo "I should be collecting logs and sending them somewhere."
}

SERVICES="tree-api"
for SERVICE in $SERVICES; do
  kubectl -n tree-api wait --for=condition=available --timeout=30s deploy/"$SERVICE" || collect_logs
done
