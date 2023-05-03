import { recorder } from "./utils/recorder";
import { sub } from "./utils/subscriber";

const { startSub, subChannel } = sub();
const { startRecorder, recordData } = recorder();

startSub(() => {
  subChannel("nas:image:ir");
  subChannel("nas:image:eo");
});

// startRecorder(() => {
//   recordData('nmea:vdm');
//   recordData('nmea:ttm');
// });
