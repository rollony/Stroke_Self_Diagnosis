import '../../App.css'
import backgroundVideo from '../../videos/video-7.mp4';
import img from '../../images/img-1.jpg';
function Home () {
    return(
        <div className='about-container'>
            <video src={backgroundVideo} autoPlay loop muted id='video'/>
            <h1>프로그램 동작 원리</h1>
            <img src ={img}></img>
            <p>설명</p>    
            
        </div>
    );
}
export default Home;