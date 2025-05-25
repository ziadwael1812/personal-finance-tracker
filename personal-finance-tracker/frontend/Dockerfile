# Stage 1: Build the React application
FROM node:18-alpine AS builder

WORKDIR /app

# Copy package.json and lock file
COPY package.json package-lock.json* pnpm-lock.yaml* yarn.lock* ./
# Choose the install command based on your package manager
# If using npm:
RUN npm install --frozen-lockfile
# If using yarn:
# RUN yarn install --frozen-lockfile
# If using pnpm:
# RUN npm install -g pnpm && pnpm install --frozen-lockfile

COPY . .

# Set build arguments for environment variables if needed
# ARG VITE_API_BASE_URL
# ENV VITE_API_BASE_URL=${VITE_API_BASE_URL}

RUN npm run build

# Stage 2: Serve the application with a lightweight server (e.g., Nginx)
FROM nginx:1.25-alpine

# Copy built assets from the builder stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy a custom Nginx configuration if needed (optional)
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80 for Nginx
EXPOSE 80

# Start Nginx when the container launches
CMD ["nginx", "-g", "daemon off;"] 