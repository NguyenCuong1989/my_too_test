# Build stage
FROM node:20-slim AS builder

WORKDIR /app

# Install dependencies with retry logic
COPY package*.json ./
RUN npm install --verbose && npm cache clean --force

# Verify npm and node
RUN node --version && npm --version

# Build TypeScript
COPY . .
RUN npm run build --verbose

# Runtime stage
FROM node:20-slim

WORKDIR /app

# Copy node_modules from builder
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package*.json ./

# Environment variables
ENV PORT=3000
ENV NODE_ENV=production

EXPOSE 3000

# Add health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=3 \
  CMD node -e "require('http').get('http://localhost:3000/', (res) => process.exit(res.statusCode === 200 ? 0 : 1)).on('error', () => process.exit(1))" || exit 1

CMD ["npm", "start"]
