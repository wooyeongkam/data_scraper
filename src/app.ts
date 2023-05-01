import { recordData } from './utils/start-record-data';
import { sub } from './utils/subscriber';

const { startSub, subChannel } = sub();
const { startRecorder, startRecordData } = recordData();

startSub(() => {
  subChannel('nas:image:ir');
  subChannel('nas:image:eo');
});

startRecorder(() => {
  startRecordData('nmea:vdm');
  startRecordData('nmea:ttm');
});
