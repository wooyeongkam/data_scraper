import { logger } from '../logger';
import { redisClient } from '../redis-config';

export const sub = () => {
  const client = redisClient.duplicate({
    legacyMode: false,
  });

  const startSub = (callback: () => void) => {
    client.on('connect', () => {
      console.log('redis Sub connected');
      callback();
    });
    client.on('error', (error) => console.log('redis Sub error'));
    client.connect();
  };

  const subChannel = async (channel: string) => {
    try {
      await client.subscribe(channel, (message) => {
        logger.info(`[${channel}]: `, { message });
      });

      console.log(channel, 'connected');
    } catch (error) {
      console.log(error);
    }
  };

  return { startSub, subChannel };
};
