import { initializeApp } from "firebase/app"
import { getAuth } from "firebase/auth"

const firebaseConfig = {
    apiKey: "AIzaSyCtbFSEloGPuWx6meLRUS-nP6Hczdxyx8I",
    authDomain: "smart-waste-management-57367.firebaseapp.com",
    projectId: "smart-waste-management-57367",
    storageBucket: "smart-waste-management-57367.appspot.com",
    messagingSenderId: "150430850891",
    appId: "1:150430850891:web:8a058ba0beef50dcb212ce",
    measurementId: "G-6BYLQYGJDG"
  };

// Initialize Firebase and Firebase Authentication
const app = initializeApp(firebaseConfig)
const auth = getAuth(app)
export {auth}