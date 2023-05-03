import { logger } from '../logger';
import { redisClient } from '../redis-config';
import sharp from 'sharp';
import fs from 'fs';

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
      await client.subscribe(channel, (message: any) => {
        if (message) {
          const buffer = Buffer.from(message['data'], 'base64');
          const image = sharp(buffer).toFile('123.jpeg');
          console.log(image);
          // fs.writeFile("123.jpeg", image, () => {});
          // image
          //   .metadata()
          //   .then((metadata) => {
          //     // fs.writeFile("123.jpeg", metadata, () => {});
          //     logger.info(`[${metadata}]: `, { message });
          //     console.log(metadata);
          //   })
          //   .catch((err) => {
          //     console.error(err);
          //   });
        }
      });

      console.log(channel, 'connected');
    } catch (error) {
      console.log(error);
    }
  };

  return { startSub, subChannel };
};

// const getBinaryImage = () => {
//   let imageUrlRef: null | string = null;
//   const urlCreator = URL;

//   const create = (arrayBuffer: string) => {
//     const blob = new Blob([arrayBuffer], { type: "image/jpeg" });
//     const imageUrl = urlCreator.createObjectURL(blob);

//     if (imageUrlRef) {
//       urlCreator.revokeObjectURL(imageUrlRef);
//     }

//     imageUrlRef = imageUrl;

//     return imageUrl;
//   };

//   return { create };
// };

// import redis from "redis";
// import sharp from "sharp";

// const client = redis.createClient({ host: "192.168.0.200", port: 30379, db: 0 });
// const channels = ["nas:image:eo", "nas:image:ir"];

// const sub_eo = redis.createClient({ host: "192.168.0.200", port: 30379, db: 0 });
// const sub_ir = redis.createClient({ host: "192.168.0.200", port: 30379, db: 0 });

// sub_eo.subscribe("nas:image:eo");
// sub_ir.subscribe("nas:image:ir");

// sub_eo.on("message", async (channel, message) => {
//   if (message) {
//     const buffer = Buffer.from(message, "base64");
//     const image = sharp(buffer);
//     image
//       .metadata()
//       .then((metadata) => {
//         // 이미지 처리 및 저장 등 원하는 작업 수행
//         console.log(metadata);
//       })
//       .catch((err) => {
//         console.error(err);
//       });
//   }
// });

// sub_ir.on("message", async (channel, message) => {
//   if (message) {
//     const buffer = Buffer.from(message, "base64");
//     const image = sharp(buffer);
//     image
//       .metadata()
//       .then((metadata) => {
//         // 이미지 처리 및 저장 등 원하는 작업 수행
//         console.log(metadata);
//       })
//       .catch((err) => {
//         console.error(err);
//       });
//   }
// });
