import React, {useState, useEffect} from 'react'
import {Link} from 'react-router-dom'
import {Button} from './Button';
import './Navbar.css';
function Navbar() {
    const [click, setClick] = useState(false);
    const [button, setButton] = useState(true);
    const handleClick = () => setClick(!click);
    const closeMobileMenu = () => setClick(false);

    const showButton = () => {
        if(window.innerWidth <= 960){
            setButton(false)
        } else{
            setButton(true)
        }
    };
    useEffect(()=>{
        showButton();
    }, []);
    window.addEventListener('resize', showButton);
    return (
        <>
            <nav className="navbar">
                <div className="navbar-container">
                    <Link to="/" className="navbar-logo" onClick={closeMobileMenu}>
                        건강한 얼굴 건강한 정신 <i class="fas fa-ambulance"></i>
                    </Link>
                    <div className='menu-icon' onClick={handleClick}>
                        <i className={click ? 'fas fa-times':'fas fa-bars'}/>
                    </div>
                    <ul className={click ? 'nav-menu active' : 'nav-menu'}>
                        <li className='nav-item'>
                            <Link to='/' className='nav-links' onClick={closeMobileMenu}>
                                홈
                            </Link>
                        </li>
                        <li className='nav-item'>
                            <Link to='/about' className='nav-links' onClick={closeMobileMenu}>
                                설명
                            </Link>
                        </li>
                        <li className='nav-item'>
                            <Link to='/qna' className='nav-links' onClick={closeMobileMenu}>
                                문의
                            </Link>
                        </li>
                    </ul>
                </div>
            </nav>
        </>
    )
}

export default Navbar
