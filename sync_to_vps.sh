#!/bin/bash

# Script to synchronize local moltbot-kimi-repo with the VPS

# Source directory on local machine
LOCAL_REPO_PATH="$(dirname "$0")"

# Destination on VPS
# CLAW_VPS is defined in the user's .zshrc as admin@100.114.222.10
REMOTE_USER_HOST="admin@100.114.222.10"
REMOTE_REPO_PATH="/home/admin/moltbot-kimi-repo/"

echo "Synchronizing local repository ($LOCAL_REPO_PATH) to VPS ($REMOTE_USER_HOST:$REMOTE_REPO_PATH)"

# Use rsync to synchronize files
# -a: archive mode (preserves permissions, timestamps, etc.)
# -v: verbose
# -z: compress file data during the transfer
# --delete: delete extraneous files from dest dirs (i.e. files that don't exist in source)
rsync -avz --delete "$LOCAL_REPO_PATH/" "$REMOTE_USER_HOST:$REMOTE_REPO_PATH"

echo "Synchronization complete."
