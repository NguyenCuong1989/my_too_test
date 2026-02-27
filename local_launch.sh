#!/bin/bash
# LOCAL SOVEREIGN MESH LAUNCHER 🚀🏗️

echo "🏗️  Starting Docker Compose (Local Mesh)..."
docker-compose -f docker-compose.yml up -d

echo "💤 Waiting for emulators to start..."
sleep 10

echo "🌱 Seeding local database..."
cd factory/mcp-router && npx ts-node src/seed_local.ts

echo "🚀 LOCAL MESH ACTIVE!"
echo "📍 Router: http://localhost:3000"
echo "📍 Emulator UI: http://localhost:4000"
echo "📍 Worker API: http://localhost:8081"
