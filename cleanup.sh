#!/bin/sh
echo "🛑 WARNING: Deleting all Docker images..."
docker rmi -f $(docker images -q)
echo "✅ All Docker images have been deleted!"
