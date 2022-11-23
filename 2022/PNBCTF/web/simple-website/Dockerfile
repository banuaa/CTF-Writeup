FROM node:18.1.0-bullseye-slim
ENV PORT=4444
WORKDIR /app
COPY ./app .
RUN npm i
CMD ["node", "main.js"]
