import '../../App.css'
import backgroundVideo from '../../videos/video-7.mp4';
function Home () {
    return(
        <div className='qna-container'>
            <video src={backgroundVideo} autoPlay loop muted id='video'/>
            <h1>개발자 연락처</h1>
            <p>이름 abcde@naver.com</p>
            <p>이름 abcde@naver.com</p>
            <p>이름 abcde@naver.com</p>
            <p>이름 abcde@naver.com</p>
            
        </div>
    );
}
export default Home;