import { uploadPhoto, createUser } from './utils.js';

export default function handleProfileSignup() {
    return Promise.all([uploadPhoto(), createUser()])
        .then((values) => {
        const photo = values[0];
        const user = values[1];

        console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
        })
        .catch(() => {
        console.log('Signup system offline');
        });
}
