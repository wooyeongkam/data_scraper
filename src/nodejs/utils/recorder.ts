import { logger } from '../logger';
import { redisClient } from '../redis-config';

export const recorder = () => {
  const client = redisClient.duplicate({
    legacyMode: true,
  });

  const startRecorder = (callback: () => void) => {
    client.on('connect', () => {
      console.log('recorder connected');
      callback();
    });
    client.connect();
  };

  const getData = async (key: string) => {
    try {
      const data = await client.v4.get(key);
      logger.info(`[${key}]: `, { message: data });
    } catch (error) {
      console.error(error);
    }
  };

  const recordData = async (key: string) => {
    setInterval(async () => await getData(key), 1000);
  };

  return { startRecorder, recordData };
};
