import ClassRoom from './0-classroom.js';

export default function initializeRooms() {
    const array = [];
    array[0] = new ClassRoom(19);
    array[1] = new ClassRoom(20);
    array[2] = new ClassRoom(34);

    return array;
}
