import React from 'react';
import '../App.css';
import {Button} from './Button';
import './HeroSection.css';
import backgroundVideo from '../videos/video-7.mp4';
import Camera, { FACING_MODES, IMAGE_TYPES } from 'react-html5-camera-photo';
import 'react-html5-camera-photo/build/css/index.css';
import Webcam from "react-webcam";
function HeroSection() {
    const webcamRef = React.useRef(null);

    const capture = React.useCallback(
        () => {
        const imageSrc = webcamRef.current.getScreenshot();
        },
        [webcamRef] 
    ); 
    const videoConstraints = {
        width: 1280,
        height: 720,
        facingMode: "user"
    };
    /*<Camera
                    onTakePhoto = { (dataUri) => { handleTakePhoto(dataUri); } }
                    onTakePhotoAnimationDone = { (dataUri) => { handleTakePhotoAnimationDone(dataUri); } }
                    onCameraError = { (error) => { handleCameraError(error); } }
                    idealFacingMode = {FACING_MODES.ENVIRONMENT}
                    idealResolution = {{width: 640, height: 480}}
                    imageType = {IMAGE_TYPES.JPG}
                    imageCompression = {0.97}
                    isMaxResolution = {true}
                    isImageMirror = {false}
                    isSilentMode = {false}
                    isDisplayStartCameraError = {true}
                    isFullscreen = {true}
                    sizeFactor = {1}
                    onCameraStart = { (stream) => { handleCameraStart(stream); } }
                    onCameraStop = { () => { handleCameraStop(); } }
                />*/
    
    return (
        <div className='hero-container'>
            <video src={backgroundVideo} autoPlay loop muted id='video'/>
            <h1>뇌졸중 초기 진단 프로그램</h1>
            <p>지금 받아보세요</p>
            <div className="hero-btns">
                <Button className="btns" buttonStyle='btn--outline' buttonSize='btn--large' onClick={capture}>사진 찍기<i className="fas fa-camera"></i></Button>
                <Button className="btns" buttonStyle='btn--outline' buttonSize='btn--large'>사진 업로드<i className="fas fa-images"></i></Button>
            </div>
            <Webcam
                    hidden={true}
                    audio={false}
                    height={720}
                    ref={webcamRef}
                    screenshotFormat="image/jpeg"
                    width={1280}
                    videoConstraints={videoConstraints}
            />
        </div>
    )
}

export default HeroSection
