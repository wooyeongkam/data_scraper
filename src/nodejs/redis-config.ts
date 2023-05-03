import * as redis from "redis";
import dotenv from "dotenv";

dotenv.config();

export const redisClient = redis.createClient({
  url: `redis://${process.env.REDIS_HOST}:${process.env.REDIS_PORT}`,
  username: process.env.REDIS_USERNAME,
  password: process.env.REDIS_PASSWORD,
  legacyMode: true,
});
